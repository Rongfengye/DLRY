Templates/DLRY is used for path issues. This is just the template folder.
Here we will create HTML files which have the capabilities of special syntax which is only in django
The idea is to make HTML that build and inherit off of each other.


<div class="row pt-5 justify-content-center">
    <div class="col"></div>
    <table class="col-sm-10 col-md-8 col-lg-4">
        {% for questRow in quests %}
            <tr class="justify-content-center text-center">
                {% for quest in questRow %}
                    <td>  
                        <p>title is {{ quest.title }}</p>
                        <p>desc is {{ quest.description }}</p>

                        <p>video URL is {{ MEDIA_URL }} {{quest.video}}</p>
                        <video autoplay="autoplay" controls="controls" preload="preload" width='320' height= '240'>
                            <source src="/DLRY{{ MEDIA_URL }}{{ quest.video }}" type='video/mp4'></source> 
                        </video>
                    </td>
                {% endfor %}
            </tr> 
        {% endfor %}

    </table>
    <div class="col"></div>
</div>

python3 -m venv DLRYvenv
source DLRYvenv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install django
python3 manage.py makemigrations DLRY
python3 manage.py migrate
python3 manage.py runserver