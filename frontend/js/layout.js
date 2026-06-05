if (localStorage.getItem("darkModeToggle") === "true") {
    document.body.classList.add("dark-mode");
}

document.body.insertAdjacentHTML("afterbegin", `
<nav class="navbar navbar-expand-lg bg-dark navbar-dark">
    <div class="container">

        <a class="navbar-brand" href="index.html">
            <img src="img/logo.png" alt="Logo" height="40">
        </a>

        <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#mainNavbar"
        >
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="mainNavbar">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link" href="index.html">Commenter</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="control.html">Contrôler</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="compress.html">Compresser</a>
                </li>
                <li class="nav-item ms-lg-5">
                    <a class="nav-link fs-5" href="settings.html" title="Réglages">
                        <i class="bi bi-gear-fill"></i>
                    </a>
                </li>
            </ul>
        </div>

    </div>
</nav>
`);

document.body.insertAdjacentHTML("beforeend", `
<footer class="bg-dark py-3 mt-auto">
    <div class="container d-flex justify-content-between">
        <a href="privacy.html" class="btn btn-outline-secondary text-white">
            Privacy & Terms
        </a>

        <span class="text-white">
            © 2026 - Dolci Marco
        </span>
    </div>
</footer>
`);

// Récupérer le nom de la page actuelle en utilisant window.location.pathname et split pour obtenir le dernier segment de l'URL
const currentPage = window.location.pathname === "/" 
    ? "index.html" 
    : window.location.pathname.split("/").pop();
document.querySelectorAll(".nav-link").forEach(link => { // Sélectionner tous les éléments avec la classe "nav-link" et itérer dessus pour vérifier si leur href correspond à la page actuelle

    const linkPage = link.getAttribute("href");

    if (linkPage === currentPage) {
        link.classList.add("active");
        link.classList.add("fw-bold");
    }
});