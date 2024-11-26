---
title: Trying QuTiP in the Browser
---

# Trying QuTiP in the Browser

QuTiP is now available in the browser!

You can open it by clicking on the button below:

<a class="btn btn-primary" href="/try-qutip/" role="button">Try QuTiP</a>

The button opens a JupyterLite notebook server with the qutip package
preinstalled. It runs entirely in your browser and includes copies of the
<a href="/qutip-tutorials/">QuTiP tutorials</a> for you to explore. There is
no server.

Once JupterLite loads, you'll find the tutorials in the file browser on
the left. If you click on a tutorial notebook, you'll need to select the
XPython kernel (there is only one option) and then the notebook will open.
The first imports will be slightly slow, but after that the performance
should be similar to that of running QuTiP locally.

Running QuTiP this way relies on a complex set of underlying layers of
software that are still maturing. You can read about some of the minor
caveats and a description of how it was built below.

Contents:

 - Caveats
 - Contributing
 - How the try-qutip site is built


## Caveats

Most QuTiP features already work. These are the known limitations:

 - A recent version of Firefox or Chrome is required.</li>
 - QobjEvo objects cannot currently be usefully compiled.</li>
 - Cython is not yet availabe.</li>
 - You can save notebooks but, they are <em>stored in your web browser's
   internal storage and might be lost if, for example, the browser cache
   is cleared. If you do create notebooks you'd like to keep, please
   use the download button to save them.</em>
  - Notebooks are slow to start, but performance is not too bad after that.
  - Having to select the XPython kernel all the time is not ideal.


## Contributing

If you encounter bugs with QuTiP in the browser that aren't listed in the
caveats above, you are welcome to open issues in the
[try-qutip GitHub repository](https://github.com/qutip/try-qutip/).

If you know a way to address any of the caveats above, please let us
know by open an issue or pull request in the
[try-qutip GitHub repository](https://github.com/qutip/try-qutip/).

If you find bugs in a specific tutorial, or would like to add a new tutorial
or improve an existing one, please see the contributing section at the bottom
of the [tutorials page](/qutip-tutorials/).

If you have general questions about how to use QuTiP, email the
[QuTiP mailing list](https://groups.google.com/group/qutip).


## How the try-qutip site is built

The try-qutip site contains JupyterLite with QuTiP pre-installed.

[JupyterLite](https://github.com/jupyterlite/jupyterlite) is a
version of [JupyterLab](https://github.com/jupyterlab/jupyterlab)
that has been modified work run in the browser as a
[Service Worker](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API).
A service worker acts like a web server that runs inside your browser and in this
case plays the role of the Jupyter server that would otherwise need to be run locally.

Running this Jupyter server in the browser means running Python and packages
such as numpy, SciPy and matplotlib in the browser too. To do that, all
of these packages need to be recompiled to
[WebAssembly (aka WASM)](https://webassembly.org/) and for
that one needs a suitable compiler, in this case,
[Emscripten](https://emscripten.org).

Lastly, we need to compile QuTiP itself. The amazing team at
[QuantStac](https://quantstack.net/) are building
[emscripten-forge](https://beta.mamba.pm/channels/emscripten-forge/packages/?tab=packages)
which is like [conda-forge](https://conda-forge.org/) but for building packages for
WebAssembly.

With the help of Wolf and Martin from QuantStack, we created a
[QuTiP package on emscripten-forge](https://beta.mamba.pm/channels/emscripten-forge/packages/qutip).
The recipe for building the package can be found in the
[emscripten-forge/recipes](https://github.com/emscripten-forge/recipes) repository.
