const form = document.getElementById("request-form");
const list = document.getElementById("request-list");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const title = document.getElementById("title").value;
  const description = document.getElementById("description").value;

  await fetch("http://127.0.0.1:5000/api/requests", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title, description })
  });

  form.reset();
  loadRequests();
});

async function loadRequests() {
    const res = await fetch("http://127.0.0.1:5000/api/requests");
    const data = await res.json();
  
    const list = document.getElementById("request-list");
    list.innerHTML = "";
  
    data.forEach((r) => {
      const li = document.createElement("li");
      li.textContent = `${r.title} [${r.status}]`;
  
      if (r.status !== "done") {
        const button = document.createElement("button");
        button.textContent = "Mark as Done";
        button.onclick = async () => {
          await fetch(`http://127.0.0.1:5000/api/requests/${r.id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ status: "done" })
          });
          loadRequests(); // Listeyi güncelle
        };
        li.appendChild(button);
      }
  
      list.appendChild(li);
    });
  }

loadRequests();