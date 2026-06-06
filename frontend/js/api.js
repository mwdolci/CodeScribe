async function callCodeScribe(endpoint) {
    const input = document.getElementById("code-input");
    const output = document.getElementById("result-output");

    output.value = "Chargement...";

    try {
        console.log("commentSize envoyé =", localStorage.getItem("commentSize"));
        const response = await fetch(`/api/${endpoint}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                code: input.value,
                comment_level: localStorage.getItem("commentLevel") || "2",
                max_comment_length: parseInt(localStorage.getItem("commentSize"), 10),
                check_syntax: localStorage.getItem("checkSyntax") !== "false",
                check_performance: localStorage.getItem("checkPerformance") !== "false",
                check_security: localStorage.getItem("checkSecurity") !== "false",
                check_best_practices: localStorage.getItem("checkBestPractices") !== "false",
                compression_level: localStorage.getItem("compressionLevel") || "2"
            })
        });

        const data = await response.json();

        if (!response.ok) {
            output.value = data.detail || "Erreur inconnue.";
            return;
        }

        output.value = data.result;
    } catch (error) {
        output.value = "Erreur de connexion avec le backend.";
    }
}

async function copyResult() {
    const output = document.getElementById("result-output");
    const text = output.value; // Récupère le texte du résultat à copier

    // Vérifie si le texte n'est pas vide ou ne contient que des espaces
    if (!text.trim()) {
        alert("Aucun résultat à copier.");
        return;
    }

    await navigator.clipboard.writeText(text); // Copie le texte dans le presse-papiers

    const copyBtn = document.getElementById("copy-btn");
    copyBtn.innerHTML = 'Copié <i class="bi bi-check2"></i>'; // Change le texte du bouton pour indiquer que c'est copié

    setTimeout(() => {
        copyBtn.innerHTML = 'Copier <i class="bi bi-copy"></i>'; // Remet le texte du bouton à la normale après 1.5 secondes
    }, 1500);
}