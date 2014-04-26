from example_app import app
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        app.run(host='0.0.0.0')
    else:
        app.run(host='0.0.0.0', port=int(sys.argv[1]))
