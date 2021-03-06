# Vizzuality Software Engineer Challenge

Challenge solution based on:

[https://github.com/Vizzuality/coding-challenge-examples/tree/software-engineer/importer](https://github.com/Vizzuality/coding-challenge-examples/tree/software-engineer/importer)

## Implementation Strategy

I am more familiar with Python because I used before in little implementations and used also pymongo when playing with tweepy. For this reason, I choose Python with Flask and pymongo for manage the POST method of the challenge since I am also more familiar in handling data than in nodejs which I have only used to do some proofs of concept. Anyway I think that is an opportunity to show my skills around the implementation of solutions with tools that I am not habituated, and of course learn and enjoy making the challenge. That's why I will use Express to implement the GET method solution.

## Software Requirements

The solution has been built with the following software:

```Docker version 17.05.0-ce```

```docker-compose version 1.21.2```

## Configuration steps
* Rename .env.dist file to .env and set the propper password for mongodb user:
```bash
MONGO_INITDB_ROOT_PASSWORD=PUT_HERE_THE_PASSWORD
MONGO_APP_USER_PASSWORD=PUT_HERE_THE_PASSWORD
```

## Docker commands

### Start containers

```docker-compose -f docker/docker-compose.yml up```

### Stop containers

```docker-compose -f docker/docker-compose.yml stop```

## Application folder structure

```
challenge/
├── docker
│   ├── data
│   ├── docker-compose.yml
│   ├── DockerfileNode
│   │   └── Dockerfile
│   └── DockerfilePython
│       └── Dockerfile
├── README.md
├── vizzuality-api-get
│   ├── index.js
│   ├── package.json
│   ├── package-lock.json
│   ├── routes
│   │   └── routes.js
│   └── tests
│       └── integration.js
└── vizzuality-api-post
    ├── app.py
    ├── dataFormatter
    │   ├── emissionsDataFormatter.py
    │   └── __init__.py
    ├── dataRetriever
    │   ├── getCsvData.py
    │   └── __init__.py
    ├── infrastructure
    │   ├── __init__.py
    │   ├── mongodbConnection.py
    │   └── mongodbPersist.py
    ├── requirements.txt
    └── tests
        ├── getCsvDataTest.py
        ├── csvDataFormatterTest.py
        └── __init__.py
```

The file structure has been created in a separate concerns way for segment logic useful for help code maintainability, extensability and testability.

## POST Method Solution

### Description

With Flask framework I created an unique POST entry point called emissions. The method parse the CSV file and persist the data into a mongodb collection.

### Simulation

For simulate a POST against the API execute the request with curl, for example, ensure replace the path to emissions.csv file:

```bash
curl -s "http://localhost:5000/emissions" \
-F file=@/path/to/emissions.csv \
-X POST \
-H 'enctype:multipart/form-data; Content-Type:multipart/form-data'
```

### Tests execution
```bash
docker exec -ti vizzuality-python-api-post sh -c "cd /opt && python -m unittest discover -s tests -p '*Test.py'"
```

### TODO List

In order to improve the solution with more time is interesting cover this implementations:

- [ ] Write more important missing unit test methods
- [ ] Improve database write with multithreading

## GET Method Solution

### Description

With a simple setup with Express I have created some trunk GET routes to retrieve information in JSON format.

### Simulation
For retrieve information against emissions dataset we have available the following entry points:

| URL | Description |
| --- | --- |
| `http://localhost:8021/api/emissions/all` | List all records |
| `http://localhost:8021/api/emissions/country/:country` | Filter records by country |
| `http://localhost:8021/api/emissions/sector/:sector` | Filter records by sector |
| `http://localhost:8021/api/emissions/parentsector/:parentsector` | Filter records by Parent sector |

### TODO List

- [ ] Create with docker environments for test and prod in order to separate software dependencies, command executions and tests execution in a more isolation way
- [ ] Entry points with params must not accept empty param
- [ ] Filter by year
- [ ] Filter by range of years
- [ ] Before test execution initialize test database with test data

### Tests execution

```bash
docker exec -ti vizzuality-nodejs-get sh -c "/home/nodejs/app/node_modules/mocha/bin/mocha /home/nodejs/app/tests/integration.js --timeout 7000"
```

## Other comments

In order to provide feedback I would like to highlight:

### Writing in mongodb

#### insert_one VS insert

In a first approach for write the data in mongodb through pymongo I used insert_one statement saving data in each iteration, this operation was spending more than 2 minutes. After thinking a little bit around how many connections are established in each iteration and in a different bulk write approach I decided store the information in one list and persist once with insert statement reducing the writing time to 1.7 seconds approximately.

### Fetch data: Firefox VS Chrome

Fetching data I am getting this disparate results in Debian stretch 64-bit PC

| URL | Browser | Version | Time |
| --- | --- | --- | --- |
| `http://localhost:8021/api/emissions/all` | Firefox Developer | 68.0b3 (64-bit) | 2.15s
| `http://localhost:8021/api/emissions/all` | Chrome | 74.0.3729.157   | 23.02s

### Express mongodb output filtering not working

When I am trying to create a filter output like:

```bash
find({},{"1950":true})
```

in correspondence with mongo client statement:

```bash
db.getCollection('emissions').find({},{"1950":true})
```

The result is incorrect

### Premature abstraction

Write tests helps me to pay more attention when I am implementing a solution, it helps me empathize better with all the elements who participate in the game: performance, complexity, quality, the test case, things that interact with, etc.

I am starting to introduce some tests, after code, and they come to me reflections or new approaches that TDD gives me, this is one important reason why practice "test first" as a primary convention in most cases.

Particularly test incosistency clears me about accidental complexity introduced in csvDataFormatter. I was using env vars in order to make more flexible the possibility of change, for example change easy via env file comma separated by tab separated as a symbol used to separate values and columns. Well, this is a possibility not a fact, I cannot know if in a future the requirements will change and introduce this new scenario, it is also a challenge, at first, without iterations. So, if I want keep simplicity I have to relate the code with the real needs instead of overtaking a non-existent possibility.
