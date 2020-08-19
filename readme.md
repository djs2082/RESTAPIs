# utility APIs

This project contains some apis developed by me as required.These apis are as follows:  
1)Corona API

Corona API:
This api shows the live cases of corona in india statewise and district wise.
it takes name of state and district as a part of url parameters and return live
corona cases in that region.


## Technologies

1)Python3  
2)Django Rest Framework  
3)Docker for Containerization  

## Installation

This project is containerized using Docker. If you have docker-compose installed on your   machine. then below command will handle depenedencies for you and start project for you.  

```bash
docker-compose up
```
if you are not having docker-compose installed, you can install dependencies with the help of   requirements.txt file provided. with below command  

```bash
pip3 install -r requirements.txt
```
## usage

This project is hosted on Heroku.com
```bash
1)http://djs-apis.herokuapp.com/state_name/district_name/  
        eg: http://djs-apis.herokuapp.com/maharashtra/nanded/  
        show cases in nanded district of maharashtra state  

2)http://djs-apis.herokuapp.com/state_name/  
        eg: http://djs-apis.herokuapp.com/maharashtra/  
        show cases in maharastra state  

3)eg: http://djs-apis.herokuapp.com/  
        eg: eg: http://djs-apis.herokuapp.com/  
        show cases throughout the country  
```

## License
[MIT](https://choosealicense.com/licenses/mit/)




