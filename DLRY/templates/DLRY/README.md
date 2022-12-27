Templates/DLRY is used for path issues. This is just the template folder.
Here we will create HTML files which have the capabilities of special syntax which is only in django
The idea is to make HTML that build and inherit off of each other.


<video autoplay="autoplay" controls="controls" preload="preload">
            <source src="{% static 'DLRY/videos/HOOPALTERCATION.mov' type='video/mp4' %}"></source> 
        </video>



<video autoplay="autoplay" controls="controls" preload="preload" width='320' height= '240'>
    <source src="HOOPALTERCATION.mov" type='video/mp4'></source> 
</video>

this works
<video autoplay="autoplay" controls="controls" preload="preload" width='320' height= '240'>
            <source src="/static/DLRY/videos/HOOPALTERCATION.mov" type='video/mp4'></source> 
        </video>


{% for quest in quests %}
            <div>
                <p>title is {{ quest.title }}</p>
                <p>desc is {{ quest.description }}</p>
                <p>video name is {{quest.video}} media is {{ MEDIA_URL }} </p>
                <!-- <source src="{{ quest.video }}" type="video/mp4"> -->
                <video autoplay="autoplay" controls="controls" preload="preload" width='320' height= '240'>
                    <source src="/static/DLRY/videos/HOOPALTERCATION.mov" type='video/mp4'></source> 
                </video>
                <p>___________________________________</p>
            </div>
        {% endfor %}

python3 -m venv DLRYvenv
source DLRYvenv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install django
python3 manage.py makemigrations DLRY
python3 manage.py migrate
python3 manage.py runserver