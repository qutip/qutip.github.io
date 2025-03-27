---
title: QuTiP in Education
layout: new_default
---

# For Educators

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

<div class="container-fluid px-0 my-center-section my-bg-secondary">
    <div class="container-xxl px-0 pb-3">
        <h2>
            QuTiP in the Classroom
        </h2>
        <p class="px-3">
            QuTiP is used by educators around the world, teaching the scientists of tomorrow.
        </p>
        <div class="slick-carousel education-carousel">
            {% for course in site.data.university_courses %}
            {% if course.visible %}
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">{{ course.institute }}</h5>
                        <p class="card-text">{{ course.course }}</p>
                        <a href="{{ course.link }}" class="card-link">Check it out!</a>
                    </div>
                </div>
            {% endif %}
            {% endfor %}
        </div>
    </div>
</div>


<div class="container-xxl mb-5">
    <h2 class="my-center-section">
        QuTiP Virtual Lab
    </h2>
    <div class="row justify-content-md-center py-3 text-image-split">
        <div class="col-md-5 mx-auto col-s-12 p-3 text">
            <h5>
                QuTiP Right From the Browser
            </h5>
            <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod.
            </p>
            <h5>
                Complex Systems Easily Explained
            </h5>
            <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod.
            </p>
            <a href="https://qutip.org/qutip-virtual-lab/" class="mx-auto mx-md-0">
                <span class="badge primary">
                    Enter QuTiP Virtual Lab
                </span>
            </a>
        </div>
        <img class="col-md-6 col-s-12 m-auto image" src="images/qutip-virtual-lab.png">
    </div>
</div>


<div class="container-fluid mb-3 px-0 my-center-section my-bg-secondary">
    <div class="container-xxl pb-3">
        <h2>
            Hand-Crafted Lectures using QuTiP
        </h2>
        <p>
            These lecture-style notebooks focus on particular quantum mechanics topics and their numerical analysis using QuTiP.
        </p>
        <ul class="list-group list-group-flush lecture-list">
            {% for lecture in site.data.lectures limit:5 %}
                <li class="list-group-item notebook-list-item">
                    <a href="{{ lecture.url }}" class="lecture-link">
                        <span>{{ lecture.title }}</span>
                        <span class="angle">&#8250;</span>
                    </a>
                </li>
            {% endfor %}
            <div class="collapse list-group-flush" id="more-items">
                {% for lecture in site.data.lectures offset:continue %}
                    <li class="list-group-item notebook-list-item">
                        <a href="{{ lecture.url }}" class="lecture-link">
                            <span>{{ lecture.title }}</span>
                            <span class="angle">&#8250;</span>
                        </a>
                    </li>
                {% endfor %}
            </div>
        </ul>
        <button class="my-3 btn-show-more" type="button" data-bs-toggle="collapse" data-bs-target="#more-items" aria-expanded="false" aria-controls="more-items" id="show-more-btn">
            Show More
        </button>
    </div>
</div>

{% include new_donate.html %}