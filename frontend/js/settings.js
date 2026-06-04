function updateCompressionLabel(value) {

        const labels = {
            1: "Faible",
            2: "Moyen",
            3: "Elevé"
        };

        document.getElementById(
            "compressionLevelValue"
        ).innerText = labels[value];
    }

// valeur initiale
updateCompressionLabel(
    document.getElementById("compressionLevel").value
);


function updateCommentLabel(value) {

        const labels = {
            1: "Léger",
            2: "Standard",
            3: "Détaillé"
        };

        document.getElementById(
            "commentLevelValue"
        ).innerText = labels[value];
    }

// valeur initiale
updateCommentLabel(
    document.getElementById("commentLevel").value
);

// Mémoriser le niveau de commentaire sélectionné dans les réglages en utilisant localStorage
const commentLevel = document.getElementById("commentLevel");
const savedLevel = localStorage.getItem("commentLevel"); // charger la valeur sauvegardée
const commentLevelValue = document.getElementById("commentLevelValue");

if (savedLevel) {
    commentLevel.value = savedLevel;
    updateCommentLabel(savedLevel); // mettre à jour le label en fonction de la valeur chargée
}

commentLevel.addEventListener("change", () => {
    localStorage.setItem("commentLevel", commentLevel.value); // sauvegarder quand ça change
    updateCommentLabel(commentLevel.value); // mettre à jour le label en fonction de la nouvelle valeur
});


const commentSize = document.getElementById("commentSize");
const commentSizeValue = document.getElementById("commentSizeValue");
const savedSize = localStorage.getItem("commentSize"); // Charger la valeur sauvegardée

if (savedSize) {
    commentSize.value = savedSize;
    commentSizeValue.innerText = savedSize;
    }

// Mise à jour en direct
commentSize.addEventListener("input", () => {
commentSizeValue.innerText = commentSize.value;
    localStorage.setItem(
        "commentSize",
        commentSize.value
    );
});

const compressionLevel = document.getElementById("compressionLevel");
const savedCompressionLevel = localStorage.getItem("compressionLevel"); // Charger la valeur sauvegardée

if (savedCompressionLevel) {
    compressionLevel.value = savedCompressionLevel;
    updateCompressionLabel(savedCompressionLevel); // mettre à jour le label en fonction de la valeur chargée
} 

compressionLevel.addEventListener("change", () => {
    localStorage.setItem("compressionLevel", compressionLevel.value); // sauvegarder quand ça change
    updateCompressionLabel(compressionLevel.value); // mettre à jour le label en fonction de la nouvelle valeur
});

// Gestion des toggles (dark mode, etc.)
const toggles = document.querySelectorAll(".setting-toggle");
toggles.forEach(toggle => {
    const savedValue = localStorage.getItem(toggle.id);

    if (savedValue !== null) {
        toggle.checked = savedValue === "true";
    }

    toggle.addEventListener("change", () => {
        localStorage.setItem(toggle.id, toggle.checked);
        if (toggle.id === "darkModeToggle") {
            document.body.classList.toggle("dark-mode", toggle.checked);
        }
    });
});