---
title: QuTiP in Education
---

# For Educators

QuTiP is a user-friendly Python library for learning and teaching quantum mechanics through simulations.
It’s ideal for exploring topics like quantum dynamics, quantum information and quantum computing.
Its visualization tools help students see how quantum systems evolve over time and understand the effects such as entanglement or decoherence.
Being open-source and part of the broader Python ecosystem, it integrates well with tools like NumPy and Matplotlib.
Educators around the world use QuTiP to create interactive examples, while students gain hands-on experience with real quantum physical models.

<div class="container-fluid px-0 my-center-section my-bg-secondary">
    <div class="container-xxl px-0 pb-3">
        <h2>
            QuTiP in the Classroom
        </h2>
        <p class="px-3">
            QuTiP is used by educators around the world, teaching the scientists of tomorrow.
        </p>
        <div class="slick-carousel education-carousel">
            {% assign courses = site.data.university_courses | where: "visible", true %}
            {% for c in courses %}
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">{{ c.institute }}</h5>
                        <p class="card-text">{{ c.course }}</p>
                        <a href="{{ c.link }}" class="card-link">Check it out!</a>
                    </div>
                </div>
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
                A simple visual tool that allows tuning and coupling of Qubits.
                Time evolutions and expectation values are automatically calculated and are ready for presentation.
            </p>
            <h5>
                Complex Systems Easily Explained
            </h5>
            <p>
                Even though quantum systems can get complicated on paper, QuTiP Virtual Lab presents a simple picture that reminds of an experimental setup.
            </p>
            <div>
                <a href="https://qutip.org/qutip-virtual-lab/" class="mx-auto mx-md-0 btn btn-primary">
                    Enter QuTiP Virtual Lab
                </a>
            </div>
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
                <li class="list-group-item notebook-list-item my-bg-secondary">
                    <a href="{{ lecture.url }}" class="lecture-link">
                        <p>{{ lecture.title }}</p>
                        <p class="angle">&#8250;</p>
                    </a>
                </li>
            {% endfor %}
            <div class="collapse list-group-flush" id="more-items">
                {% for lecture in site.data.lectures offset:continue %}
                    <li class="list-group-item notebook-list-item my-bg-secondary">
                        <a href="{{ lecture.url }}" class="lecture-link">
                            <p>{{ lecture.title }}</p>
                            <p class="angle">&#8250;</p>
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

{% include donate.html %}