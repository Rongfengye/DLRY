Templates/DLRY is used for path issues. This is just the template folder.
Here we will create HTML files which have the capabilities of special syntax which is only in django
The idea is to make HTML that build and inherit off of each other.


<p>video URL is {{ MEDIA_URL }} {{quest.video}}</p>
                <video autoplay="autoplay" controls="controls" preload="preload" width='320' height= '240'>
                    <source src="/DLRY{{ MEDIA_URL }}{{ quest.video }}" type='video/mp4'></source> 
                </video>

python3 -m venv DLRYvenv
source DLRYvenv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install django
python3 manage.py makemigrations DLRY
python3 manage.py migrate
python3 manage.py runserver