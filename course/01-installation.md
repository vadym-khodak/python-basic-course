# Встановлення Python

## Встановлення Python на macOS

- відкрити `Terminal`:
  - натиснути`Command + Space`
  - у полі пошуку ввести `Terminal`
  - вибрати зі списку `Terminal`
  ![Find Terminal](images/find_terminal.png)

- перевірити поточну версію Python в Terminal
    ```bash
    python --version
    ```

### Встановлення віртуального оточення
- встановлення `pyenv`
    ```bash
    brew install pyenv
    ```
- встановлення pyenv-virtualenv
    ```bash
    brew install pyenv-virtualenv
    ```

- встановлення необхідної версії Python в `pyenv`
    ```bash
    pyenv install <necessary python version> 
    ```
    > Приклади `<necessary python version>`: `3.8.0`, `3.6.5`, `2.7.3`

- створення віртуального оточення використовуючи `pyenv`
    ```bash
    pyenv virtualenv <necessary python version> <virtualenv name>
    ```
    >`necessary python version` повинна бути встановлена як це зазначено у попередньому пункті
    >
    >Приклади `virtualenv name`: `test`, `pet_project`, `my_app`.
    
    >Якщо Ви отримали помилку:
    ```
    Failed to activate virtualenv.
    
    Perhaps pyenv-virtualenv has not been loaded into your shell properly. Please restart current shell and try again.
    ```
    >Вам необхідно додати наступні рядки до `.bashrc` файлу та перезавантажити його:
    ```bash
    echo 'eval "$(pyenv init -)"' >> .bashrc
    echo 'eval "$(pyenv virtualenv-init -)"' >> .bashrc
    source ~/.bashrc
    ```

- активація віртуального оточення використовуючи `pyenv`
    ```bash
    pyenv activate <virtualenv name>
    ```

- деактивація віртуального оточення використовуючи `pyenv`
    ```bash
    pyenv deactivate 
    ```

- запуск інтерпретатора Python в інтерактивному режимі
    ```bash
    python
    ```

- закриття інтерпретатора Python в інтерактивному режимі
`Control + D`

- запуск файла Python в Terminal
    ```bash
    python <path to python file>  # ~/Desktop/hello.py
    ```

## Встановлення Python на Linux
