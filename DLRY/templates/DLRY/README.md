Templates/DLRY is used for path issues. This is just the template folder.
Here we will create HTML files which have the capabilities of special syntax which is only in django
The idea is to make HTML that build and inherit off of each other.


<video autoplay="autoplay" controls="controls" preload="preload">
            <source src="{% static 'DLRY/videos/HOOPALTERCATION.mov' type='video/mp4' %}"></source> 
        </video>
