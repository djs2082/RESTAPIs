#utility apis
    This project contains some apis developed by me as required.These apis are as follows:
    1)Corona API


 Corona API:
        This api shows the live cases of corona in india statewise and district wise.
        it takes name of state and district as a part of url parameters and return live
        corona cases in that region.


#Technologies
    Python3
    Django Rest Framework
    Docker for Containerization

##Installation
    This project is containerized using Docker. If you have docker-compose installed on your machine. then just a 'docker-compose up' command will handle depenedencies for you and start project for you.

    if you are not having docker-compose installed, you can install dependencies with the help of requirements.txt file provided. command is 'pip3 install -r requirements.txt'

##usage
    This project is hosted on Heroku.com
    urls:
    1)http://djs-apis.herokuapp.com/<state-name>/<district-name>/
            eg: http://djs-apis.herokuapp.com/maharashtra/nanded/
            show cases in nanded district of maharashtra state
    
    2)http://djs-apis.herokuapp.com/<state-name>/
            eg: http://djs-apis.herokuapp.com/maharashtra/
            show cases in maharastra state

    3)eg: http://djs-apis.herokuapp.com/
            eg: eg: http://djs-apis.herokuapp.com/
            show cases throughout the country




