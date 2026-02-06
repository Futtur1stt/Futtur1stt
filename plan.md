# Дорожная карта: Браузерный JavaScript за 4 недели (3–4 ч/день)

- Формат: 6 дней в неделю, 1 день — отдых/буфер. Каждый день: 90–120 мин теории + конспект, 60–120 мин практики/упражнений, 15–30 мин рефактор/коммиты.
- Инструменты: без сборщиков (Vite/npm) на этом этапе. Запуск через простой сервер, иначе CORS и file:// создадут проблемы.
  - Быстрый старт сервера: `python3 -m http.server 5173` и открыть `http://localhost:5173`
  - Или VS Code Live Server.

## Содержание
- Неделя 1 (Дни 1–6): DOM, события, формы/валидация, ошибки (try/catch), RegExp 80/20, утилиты (debounce/throttle, rAF)
- Неделя 2 (Дни 7–12): API/HTTP/REST, Fetch + CORS, Promises, async/await, Abort/timeout/retry, Web Storage, URL/History, ES‑modules, DevTools
- Неделя 3: Проект 1 — «Умная форма» (регистрация/заказ)
- Неделя 4: Проект 2 — «Каталог по публичному API» (DummyJSON)
- Критерии качества и контрольные точки

---

## Ссылки-источники (используются в плане)
- MDN DOM/Element/DocumentFragment: https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model
- JS.info DOM: https://javascript.info/dom-navigation, https://javascript.info/modifying-document
- MDN События: https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener
- MDN Keyboard/Focus: https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent
- MDN Forms/Validation: https://developer.mozilla.org/en-US/docs/Learn/Forms, https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation
- MDN ValidityState: https://developer.mozilla.org/en-US/docs/Web/API/ValidityState
- MDN aria-live: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-live
- JS.info Ошибки: https://javascript.info/try-catch, https://javascript.info/custom-errors
- MDN try...catch, Error: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch
- MDN RegExp Guide: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions
- MDN rAF/setTimeout: https://developer.mozilla.org/en-US/docs/Web/API/window/requestAnimationFrame
- web.dev Long tasks: https://web.dev/optimize-long-tasks/
- web.dev Lighthouse: https://developer.chrome.com/docs/lighthouse/overview/
- web.dev Learn Accessibility: https://web.dev/learn/accessibility/
- MDN HTTP Overview/Methods/Status/Headers: https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview
- Postman What is a REST API?: https://learning.postman.com/docs/introduction/overview/
- MDN Fetch: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
- MDN CORS: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
- JS.info Fetch: https://javascript.info/fetch
- JS.info Promises/Microtasks/Async: https://javascript.info/promise-basics, https://javascript.info/promise-chaining, https://javascript.info/microtask-queue, https://javascript.info/async-await
- MDN Promise utils: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise
- MDN AbortController: https://developer.mozilla.org/en-US/docs/Web/API/AbortController
- MDN Web Storage: https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API
- MDN History API: https://developer.mozilla.org/en-US/docs/Web/API/History_API
- MDN URLSearchParams: https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams
- MDN ES Modules: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules
- MDN import/export: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import
- Chrome DevTools: https://developer.chrome.com/docs/devtools/
- DummyJSON docs: https://dummyjson.com/docs/products
- ReqRes (мок‑API): https://reqres.in/

---

## Неделя 1 — Теория (Дни 1–6)

### День 1 — DOM: поиск и изменение
- Теория: MDN DOM/Element/DocumentFragment; JS.info навигация/изменение документа (ссылки выше).
- Упражнения:
  1) Создать `index.html`, `styles.css`, `js/day1.js` (подключить `<script type="module">`). В HTML — контейнер `<div id="list"></div>`.
  2) В `js/day1.js`:
     - Объявить массив из 5–10 объектов `{ id, title, price }`.
     - Функция `renderCard(item)` — создает DOM‑узел карточки через `document.createElement`, устанавливает текст/классы.
     - Функция `renderList(items, container)`: создать `DocumentFragment`, пройтись по `items`, `frag.append(renderCard(i))`, затем `container.replaceChildren(frag)`.
  3) Критерии: без инлайн-обработчиков в HTML; рендер одним вызовом `renderList`.

### День 2 — События и делегирование
- Теория: MDN addEventListener, всплытие/захват, KeyboardEvent, основы фокуса.
- Упражнения:
  1) Делегирование кликов: навесить один `click`‑слушатель на контейнер списка, находить карточку через `event.target.closest('.card')`.
  2) Клавиатурная навигация: обработчик `keydown` на контейнере; по ArrowDown/ArrowUp переводить фокус на соседнюю карточку (через `tabindex` и `focus()`).
  3) Критерии: мышь и клавиатура работают; один слушатель на контейнере.

### День 3 — Формы и валидация
- Теория: MDN Forms, FormData, Constraint Validation API, ValidityState, aria‑live.
- Упражнения:
  1) Разметка формы: поля `name`, `email`, `password`, чекбокс согласия; блок ошибок `<div role="status" aria-live="polite" id="errors"></div>`.
  2) JS: по `submit` собрать `FormData`, для каждого поля если пусто — `setCustomValidity('…')`, иначе `''`; если форма невалидна — `form.reportValidity()` и фокус на первом невалидном.
  3) Выводить краткое сводное сообщение об ошибках в `#errors`.
  4) Критерии: валидные сообщения, доступный вывод, корректный фокус.

### День 4 — Ошибки (try/catch) + RegExp 80/20
- Теория: JS.info try/catch и пользовательские ошибки; MDN Error; RegExp (классы/квантификаторы/якоря/флаги).
- Упражнения:
  1) `parseJsonSafe(str)`: `try { JSON.parse } catch (e) { return { ok:false, error:e.message } }` иначе `{ ok:true, data }`.
  2) `class ValidationError extends Error { constructor(msg, field){ super(msg); this.name='ValidationError'; this.field=field; } }` — генерируй при проверках формы и показывай понятные сообщения.
  3) Нормализация телефона: `s.replace(/\D+/g,'')`; простая проверка email: `/^\S+@\S+\.\S+$/`.
  4) Критерии: падения нет, ошибки локализованы, сообщения читабельные.

### День 5 — Утилиты: debounce/throttle, requestAnimationFrame
- Теория: rAF и таймеры; оптимизация длинных задач (web.dev).
- Упражнения:
  1) Реализовать `debounce(fn, ms)` (вызов через `ms` после последнего события) и `throttle(fn, ms)` (не чаще 1 раза в `ms`).
  2) Применить debounce к `input` поиска — логировать запрос только после паузы.
  3) Маленькая анимация через rAF (плавный счетчик/прогресс‑бар).
  4) Критерии: нет «спама» обработчиками; анимация плавная.

### День 6 — Повтор и качество
- Теория: Lighthouse, a11y чек‑лист (web.dev).
- Упражнения:
  1) Проверить разметку: один `h1`, корректная иерархия заголовков, видимый фокус, контраст.
  2) Запустить Lighthouse (моб.) и зафиксировать метрики.
  3) Критерии: A11y/Best Practices ≥ 90 (на текущей болванке/демо).

---

## Неделя 2 — Теория (Дни 7–12)

### День 7 — API/HTTP/REST (концепции)
- Теория: MDN HTTP overview/methods/status/headers; Postman — что такое REST API.
- Упражнения:
  1) Создать `notes.md` и описать 5 эндпоинтов DummyJSON: список, поиск, категории, категория по имени, деталь; привести примеры URL с `limit/skip`.
  2) Для каждого эндпоинта — метод, пример запроса и полей ответа.
  3) Критерии: понимаешь path vs query, коды 2xx/4xx/5xx и их смысл.

### День 8 — Fetch и CORS
- Теория: MDN Fetch, CORS; JS.info Fetch.
- Упражнения:
  1) Написать `loadProducts(limit=10)`: `fetch(url)`, проверка `res.ok`, `await res.json()`.
  2) Мини‑UI статусов: показать `loading → success` (3 элемента) → `empty` (если пусто) → `error` (если 4xx/5xx/сеть).
  3) Критерии: разные статусы отрабатывают, ошибки не роняют приложение.

### День 9 — Promises и async/await
- Теория: состояния, цепочки, микрозадачи; async/await; Promise utils (`all`, `allSettled`, `race`, `any`).
- Упражнения:
  1) Последовательно: запрос продуктов, затем категорий — замерь время.
  2) Параллельно через `Promise.all` — замерь время и сравни.
  3) Перепиши then‑цепь на `async/await + try/catch`.
  4) Критерии: параллель используется корректно; один локальный `catch`.

### День 10 — AbortController, таймауты, ретраи
- Теория: MDN AbortController, abort signals.
- Упражнения:
  1) `withTimeout(promise, ms)` через `Promise.race` с таймаут‑промисом.
  2) `retry(fn, { attempts=3, backoffMs=500 })` — экспоненциальный backoff.
  3) Поле поиска: отменять предыдущий `fetch` через `AbortController` при следующем вводе.
  4) Критерии: отмены не помечаются «красными» ошибками; есть кнопка «Повторить».

### День 11 — Web Storage + URL/History
- Теория: MDN Web Storage, History API, URLSearchParams.
- Упражнения:
  1) TTL‑кэш: `setCache(key, data, ttlMs)` — сохранять `data` с `expiresAt`; `getCache(key)` возвращает `null`, если протух.
  2) Синк состояния с URL: сериализовать `q`, `category`, `page` в `?`‑строку, `pushState`, обрабатывать `popstate`.
  3) Критерии: back/forward восстанавливает UI; мгновенный показ из кэша + фоновое обновление.

### День 12 — ES‑modules и DevTools
- Теория: MDN Modules/import/export/dynamic import; DevTools Network/Performance/Coverage.
- Упражнения:
  1) Разнести код на модули: `js/utils/{debounce.js, throttle.js, retry.js, withTimeout.js}`, `js/api/products.js`, `js/ui/{renderList.js, renderCard.js}`, `js/state/{url.js, storage.js}`. В HTML — `<script type="module" src="js/main.js"></script>`.
  2) В `main.js` импортировать нужные функции; сделать 1 динамический импорт (ленивая загрузка форматтера) по клику.
  3) DevTools: проверить waterfall (Network), long tasks (Performance), лишний код (Coverage).
  4) Критерии: всё работает на статическом сервере; без глобальных переменных.

---

## Неделя 3 — Проект 1: «Умная форма» (регистрация/заказ)

### Цели
- Отработать формы, валидацию, обработку ошибок, POST‑запросы, отмену запросов, сохранение черновика, доступность.

### Технологии
- Ванильный JS + HTML + SCSS(BEM) (или CSS). Без сборщика. Простые ES‑модули.

### ТЗ (MVP)
- Поля: имя, email, телефон (нормализация или маска), пароль и подтверждение, чекбокс согласия.
- Валидация: встроенная (required, pattern) + кастомная через `setCustomValidity`; общий блок ошибок `aria-live`.
- Отправка: POST на ReqRes `/api/users` или `/api/register`; состояния UI: idle/loading/success/error; кнопка «Повторить».
- Отмена: `AbortController` при повторных сабмитах.
- Черновик: авто‑сохранение введенных значений в `localStorage` (с TTL 1–7 дней), кнопка «Сбросить».
- A11y: правильные `label for`, порядок табов, видимый фокус, контрасты.

### Структура
- `index.html`, `styles/`, `js/`
  - `js/api.js` — `postJSON(url, body, { signal })` с `fetch + withTimeout + retry` и проверкой `res.ok` → `Error('HTTP …')`
  - `js/validation.js` — функции проверки полей (в т.ч. `ValidationError`)
  - `js/ui.js` — показ ошибок, состояния загрузки/успеха/ошибок
  - `js/draft.js` — get/set черновика в `localStorage` с TTL
  - `js/main.js` — инициализация слушателей, сборка `FormData`, управление `AbortController`

### Этапы реализации (по дням недели 3)
1) День 13: Спецификация полей/ошибок, макет/семантический HTML, базовые стили и фокус. Подключить `type="module"`.
2) День 14: Валидация: встроенная + кастомные тексты, `aria-live` для ошибок, нормализация телефона.
3) День 15: `api.js`: POST на ReqRes с `withTimeout` и `retry`; в UI — idle/loading/success/error, дизейбл кнопки, «Повторить».
4) День 16: `AbortController` — отмена предыдущего сабмита; `draft.js` — автосохранение и «Сбросить».
5) День 17: A11y/Perf: Lighthouse ≥ 90 (мобайл), убрать лишние reflow, поправить контраст/фокус.
6) День 18: README (цель, стек, фичи, как запустить, скриншоты, демо), деплой на GitHub Pages.

### Критерии приёмки
- Валидация без сторонних библиотек; понятные сообщения; `aria-live`.
- Отмена/повтор запросов; корректная обработка ошибок сети/HTTP.
- Черновик работает, не ломает валидацию.
- Lighthouse (моб.) A11y/Best ≥ 90. README и демо присутствуют.

---

## Неделя 4 — Проект 2: «Каталог по публичному API» (DummyJSON)

### Цели
- Списки, поиск/фильтры/пагинация, кэш + SWR, отмена/ретраи/таймаут, синхронизация с URL, модульная архитектура ES‑modules.

### API
- База: `https://dummyjson.com/products`
  - GET `/products?limit=..&skip=..`
  - GET `/products/search?q=..`
  - GET `/products/categories`
  - GET `/products/category/{name}`
  - GET `/products/{id}`

### ТЗ (MVP)
- Главная: список карточек товаров, фильтр по категории, поиск по строке, пагинация.
- Деталь: страница продукта с данными (`/products/{id}`).
- Состояния: скелетоны, пусто, ошибка, «повторить».
- Кэш: last‑response в `localStorage` (TTL 10–30 сек) + SWR (показываем кэш сразу и фоново обновляем).
- Отмена: `AbortController` при новом поисковом запросе; таймаут и ретраи для устойчивости.
- URL‑синк: `?q=&category=&page=`; поддержка back/forward (`popstate`).

### Структура
- `index.html`, `product.html`, `styles/`, `js/`
  - `js/api/products.js` — все запросы (list/search/categories/detail) + withTimeout/retry/abort
  - `js/ui/{list.js, card.js, detail.js}` — рендер
  - `js/state/{url.js, storage.js}` — синхронизация состояния и кэш
  - `js/utils/{debounce.js, retry.js, withTimeout.js}`
  - `js/main.js` (главная), `js/product.js` (деталь)

### Этапы реализации (по дням недели 4)
1) День 19: ТЗ, каркас HTML (главная и деталь), базовый SCSS(BEM), структура папок.
2) День 20: Рендер списка + скелетоны, пагинация (UI), базовый поиск (input + debounce), делегирование кликов.
3) День 21: `api/products.js` с abort/timeout/retry; кэш TTL + SWR (показываем кэш → обновляем фоном → мягко обновляем список).
4) День 22: Фильтр по категории + URL‑синк (`URLSearchParams`, `pushState`, `popstate`), страница детали (`/products/{id}`), параллелить независимые запросы через `Promise.all`.
5) День 23: Состояния пусто/ошибка, «повторить», responsive images (`srcset/sizes`), шрифты `woff2` + `font-display: swap`; Lighthouse ≥ 90.
6) День 24: README (демо, стек, фичи, параметры URL, ограничения), деплой (GitHub Pages или Netlify без сборки).

### Критерии приёмки
- Модули разделены по слоям (`api/ui/state/utils`).
- URL back/forward восстанавливает состояние.
- Устойчивость к сети: отмена, таймаут, ретраи; кэш + SWR.
- Lighthouse (моб.) A11y/Best ≥ 90. README и демо присутствуют.

---

## Общие критерии «готово»
- Код чистый, модульный, без глобальных переменных.
- A11y: семантика, фокус, контрасты, навигация с клавиатуры.
- README в каждом проекте: цель, стек, фичи, демо, запуск, скриншоты.
- Деплой: GitHub Pages/Netlify (без сборщиков).
- Мини‑чек‑листы ручного тестирования:
  - Форма: пустые/невалидные, отмена, повтор, черновик, сеть down.
  - Каталог: быстрый ввод (отмена), смена категорий, пагинация, back/forward, оффлайн (кэш), ошибки сети (ретраи).