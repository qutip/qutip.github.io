---
title: QuTiP Ecosystem
---

# Scientific Packages Powered by QuTiP

Here we catalogue independent, actively maintained Python packages published on PyPI that are compatible with or built on QuTiP. Each entry excludes internal QuTiP packages (such as qutip-qip or qutip-jax), meets continuous maintenance standards. Built something with QuTiP? We'd love to list it here. See the [contribution guidelines](https://github.com/qutip/qutip.github.io#adding-a-new-package-to-ecosystem-page) to add your package.


<section class="container-fluid my-bg-secondary py-4">
  <div class="container-xxl">
    <div class="mb-4">
        <h1 class="pb-4 text-center">Ecosystem</h1>
        <select class="form-select mx-auto" style="max-width: 300px;"  id="domainFilter" onchange="filterCards(this.value)">
            <option value="all">All Domains</option>
            {%- for d in site.data.domain -%}
            <option value="{{ d.domain }}">{{ d.domain }}</option>
            {%- endfor -%}
        </select>
    </div>
    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-4" id="card-grid"> 
        {% for p in site.data.packages%}
        <div class="col" data-domain="{{ p.domain }}">
            <div class="card shadow-sm h-100 border-dark">
            <div class="card-body d-flex flex-column">
                <h5 class="card-title pb-2">
                    {{ p.name }}
                </h5>
                <h6 class="card-subtitle mb-2 text-muted text-uppercase subtitle-sm  border-bottom mb-3">
                    {{ p.domain }}
                </h6>
                <p class="card-text text-muted clamp-3 mb-1">
                    {{ p.description }}
                </p>
                <a tabindex="0" 
                role="button" 
                class="small align-self-end mb-3 read-more"
                data-bs-toggle="popover"
                data-bs-trigger="focus"
                data-bs-placement="top"
                data-bs-title="Description"
                data-bs-custom-class="desc-popover"
                data-bs-content="{{ p.description | escape }}">
                    Read more
                </a>
                <div class="mt-auto d-flex justify-content-between align-items-center border-top pt-2">
                    <div class="flex-shrink-0">
                        <a href="https://pypi.org/project/{{p.pypi}}" target="_blank" rel="noopener noreferrer" class="card-link mt-auto small">PyPI</a>
                        <a href="https://github.com/{{p.github}}" target="_blank" rel="noopener noreferrer" class="card-link mt-auto small">GitHub</a>
                    </div>
                <small class="text-body-tertiary text-truncate ms-2">{{ p.organization }}</small>
                </div>
            </div>
            </div>
        </div>
        {% endfor %}
    </div>
  </div>
</section>


{% include supp_org.html %}
{% include sponsor.html %}