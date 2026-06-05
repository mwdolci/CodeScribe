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
                max_comment_length: parseInt(localStorage.getItem("commentSize"), 10)
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