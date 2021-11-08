# Git / GitHUb

## Конфігурація глобальних налаштувань користувача
```bash
git config --global user.name "<YOUR USER NAME>"
git config --global user.email "<YOUR@EMAIL>COM>"
```

## Список популярних команд що використовуються у різних ситуаціях (використовуйте `git help`):

### Створення робочого простору:
- клонування репозиторія в нову папку
    ```bash
    git clone https://github.com/<your-github-username>/<your-github-repository>.git
    ```
- створення нового пустого репозиторія або переініціалізація наявного
    ```bash
    git init
    ```
### Робота над поточними змінами:
- додавання файлу/файлів до індексу
    ```bash
    git add --all .  # додавання всіх файлів
    git add main.py  # додавання одного файлу `main.py`
    ```
- переміщення/перейменування файлу/папки
    ```bash
    git mv main.py app.py
    ```
- видалення файлу з робочого дерева та з індексу
    ```bash
    git rm app.py
    ```

### Перевірка історії та статусу:
- показати різницю між коммітами
    ```bash
    git diff
    ```
- вивести строки що сходяться зі зразком
    ```bash
    git grep --text <some-text>
    ```

- вивести лог коммітів
    ```bash
    git log
    ```

- вивести статус робочого дерева
    ```bash
    git status
    ```

### Розвивати, відзначати та змінювати історію репозиторія
- робота з гілками робочого дерева
    ```bash
    git branch --list                # вивести список гілок
    git branch <new-branch-name>     # створити нову гілку
    git branch <new-branch-name> -d  # видалити гілку
    ```

- створити новий комміт
    ```bash
    git commit -m "Some message"
    ```

collaborate (see also: git help workflows)
- завантажити об'єкти та посилання з іншого репозиторія
    ```bash
    git fetch
    ```
- отримати та інтегрувати з іншим сховищем або локальною гілкою
    ```bash
    git pull
    ```
- оновлення віддалених посилань разом із пов’язаними об’єктами
    ```bash
    git push -u origin master
    ```

## Створення нового репозиторія використовуючи термінал
```bash
echo "# My New Repository" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/<your-github-username>/<your-github-repository>.git
git push -u origin main
```

## Використання глобального gitignore
```bash
echo ".idea" >> ~/.gitignore_global
git config --global core.excludesfile ~/.gitignore_global
```

## Корисні посилання
- [Git - Lecture 1 - CS50's Web Programming with Python and JavaScript 2020](https://youtu.be/NcoBAfJ6l2Q) - English
- [Створити GitHub repo](https://docs.github.com/en/get-started/quickstart/create-a-repo)
- [Про Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
- [Створення Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)


## Домашнє завдання:
### Звичайний рівень
1. Клонувати цей репозиторій
2. Створити новий репозиторій локально
3. Додати в репозиторій `.gitgnore`
4. Додати в репозиторій `README.md`
5. Додати в репозиторій файл `hello.py`
6. Створити репозиторій в GitHub
7. Зв'язати локальний репозиторій з репозиторієм в GitHub
8. Оновити віддалений репозиторій 
9. Надати користувачу `vadym-khodak` доступ до Вашого GitHub репозиторія

### Advance: Зробити оновлення віддаленого репозиторія використовуючи GitHub Pull Request.
1. Додати в локальний репозиторій файл main.py
2. Зробити Pull Request у GitHub для оновлення віддаленого репозиторія.
3. Відправити користувачу vadym-khodak запит на перевірку цього Pull Request
4. Залишити коментар до Pull Request у якому позначити користувача vadym-khodak
