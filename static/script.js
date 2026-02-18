function generate() {
  const length = document.getElementById("length").value;
  const result = document.getElementById("result");
  const error = document.getElementById("error");

  result.textContent = "";
  error.textContent = "";

  if (!length) {
    error.textContent = "Password length is required.";
    return;
  }

  fetch("/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ length })
  })
    .then(res => res.json())
    .then(data => {
      if (data.error) {
        error.textContent = data.error;
      } else {
        result.textContent = data.password;
      }
    });
}
