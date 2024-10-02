# Joke Fetcher API

## Description

This is a simple Python project that fetches random jokes from the [JokeAPI](https://jokeapi.dev/). The user can choose between four categories of jokes:

1.  **Programming** - Jokes related to programming and developers.
2.  **Dark** - Dark humor jokes.
3.  **Christmas** - Christmas-themed jokes.
4.  **Any** - A random joke from any category.

The program will fetch a joke from the selected category and display it in the terminal.

## Features

-   Choose between multiple categories of jokes.
-   Fetch and display jokes from the **JokeAPI**.
-   Simple command-line interface.

## Installation

### Prerequisites

-   Python 3.x
-   requests library (for making HTTP requests)

### Install Dependencies

Make sure to install the required Python packages:

```bash
pip install requests
````

## Usage

1.  Run the Python script:

```bash
python joke\_fetcher.py
```
You will be prompted to choose a category:
Choose a joke category:
1. Programming
2. Dark
3. Christmas
4. Any

**Secret Note:** You can type anything to search for that topic 

Enter the number corresponding to the category you want, and a joke will be fetched from JokeAPI and displayed.

### Example Output

If you choose the **Programming** category, the output might look like this:

Here's a Programming Joke:
"Why do programmers prefer dark mode? Because the light attracts bugs."
    

## Joke Categories

-   **Programming**: Jokes about programmers, coding, and software development.
-   **Dark**: Jokes with dark humor.
-   **Christmas**: Fun and festive jokes for the holiday season.
-   **Any**: Fetches a joke from any available category.

## API

This project uses the [JokeAPI](https://jokeapi.dev/) to fetch jokes. No registration or API key is required to use this API.

## Contributing

Contributions are welcome! If you have suggestions for improving the project, feel free to open an issue or submit a pull request.

1.  Fork the repository.
2.  Create a new branch (git checkout -b feature-branch).
3.  Make your changes.
4.  Push the branch (git push origin feature-branch).
5.  Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

-   [JokeAPI](https://jokeapi.dev/) for providing the jokes.
-   [Python Requests Library](https://docs.python-requests.org/) for handling API requests.