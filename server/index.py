from app import app


# This code block is checking if the current script is being run as the main program (as opposed to
# being imported as a module into another program). If it is being run as the main program, it will
# execute the `app.run()` method with the `debug` parameter set to `True`, which starts the Flask
# application in debug mode.
if __name__ == "__main__":
    app.run(debug=True)
