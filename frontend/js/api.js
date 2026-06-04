async function callCodeScribe(endpoint) {
    const input = document.getElementById("code-input");
    const output = document.getElementById("result-output");

    output.value = "Chargement...";

    try {
        const response = await fetch(`/api/${endpoint}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                code: input.value,
                language: "python"
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