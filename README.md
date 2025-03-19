# Всем добро пожаловать в репозиторий с заданиями по направлению MLOps в AI Lab SDU!

### Ссылки:
[Task 1](./lab1/LabTask.md)

### Как тут работать?

- #### Склонируйте эту репу 
    ```
    git clone https://github.com/SultanMukashev/AILabEngineers.git
    ```
- #### Локально у себя откройте новую ветку(branch)
    ```
    git branch -c 'your-unique-branch-name'
    ```
- #### Когда захотите сделать изменения используйте:

    ##### Добавление изменений:
        git add path-to-your-file
    Examples:
    - Adding all changes in your working directory in terminal
        
        ```
        git add .
        ```
        - Adding exact files
        ```
        git add file1 file2 dir1/file3
        ```
     ##### Коммиты для сохранения состояния для будущих откатов, чем чаще при мелких но важных изменениях, тем лучше.

        git commit -m 'your commit message'

    Examples:
    ```
    git commit -m 'fix: changed configuration file
    ```

    ```
    git commit -m 'feat: added new function for parsing'
    ```

    ##### Пуш изменений в свой бранч на удаленный гитхаб репо чтобы другие видели

    ```
    git push origin your-unique-branch-name 
    ```

- #### Если будут супер большие файлы или папки, добавляйте пути к ним в .gitignore файл. Например pgdata где хранятся данные с постгреса.

