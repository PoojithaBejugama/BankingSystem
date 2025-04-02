
## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/projectfile
    cd BankingSystem
    ```

## Running the FastAPI Server
###Environment Setup
1. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

     If you get scripts are disabled error, use this command: 
        ```bash
        Set-ExecutionPolicy Unrestricted -Scope Process
        ```
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
1. Start the FastAPI server using Uvicorn:
    ```bash
    uvicorn main:app --reload
    ```

2. Your API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

3. You can check the automatic API docs at:
    - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - Redoc UI: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Testing

1. To run the tests, use:
    ```bash
    pytest
    ```

## Running the React Frontend

1. Navigate to the frontend directory:
    ```bash
    cd frontend
    ```

2. Install the dependencies:
    ```bash
    npm install
    ```

3. Start the development server:
    ```bash
    npm run dev
    ```

4. Your React application will be available at: [http://localhost:3000](http://localhost:3000)


## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


