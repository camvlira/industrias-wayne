async function login(){
  const username= document.getElementById("username").value
  const password= document.getElementById("password").value

  const res = await fetch("http://localhost:5000/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  })

  const data= await res.json()
  if (res.ok){
    localStorage.setItem("token", data.token)
    localStorage.setItem("nome", data.nome)
    localStorage.setItem("cargo", data.cargo)
    window.location.href = "dashboard.html"
  } else {
    document.getElementById("error").textContent = data.error
  }
}
async function logout(){
  localStorage.clear()
  window.location.href = "index.html"
}
async function carregarDashboard(){
  const nome = localStorage.getItem("nome")
  const cargo = localStorage.getItem("cargo")
  const token = localStorage.getItem("token")
  if (!token) return logout()

  document.getElementById("nome-usuario").textContent = nome

  const resRecursos = await fetch("http://localhost:5000/recursos", {
    headers: { Authorization: `Bearer ${token}` },
  })
  const recursos = await resRecursos.json()

  document.getElementById("total-recursos").textContent = recursos.length
  document.getElementById("total-funcionarios").textContent = "4" 

  const atividades= [
    `Usuário ${nome} fez login`,
    "Recurso 'Batmóvel' adicionado",
    "Recurso 'Rastreamento' removido",
    "Usuário funcionario fez login",
  ]
  const listaAtividades= document.getElementById("lista-atividades")
  listaAtividades.innerHTML = ""
  atividades.forEach(a => {
    const li = document.createElement("li")
    li.textContent = a
    listaAtividades.appendChild(li)
  })

  const tiposCount = {}
  recursos.forEach(r => {
    tiposCount[r.tipo] = (tiposCount[r.tipo] || 0) + 1
  })

  const ctx = document.getElementById("grafico-recursos").getContext("2d")
  new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: Object.keys(tiposCount),
      datasets: [
        {
          label: "Tipos de Recursos",
          data: Object.values(tiposCount),
          backgroundColor: ["#988829", "#4a90e2", "#1e253eff"],
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: "bottom",
          labels: { color: "#eee"},
        },
      },
    },
  })

  if (cargo !== "admin"){
    document.getElementById("acoes-admin").style.display = "none"
  }
  const lista = document.getElementById("lista-recursos")
  lista.innerHTML= ""
  recursos.forEach(r => {
    const div = document.createElement("div")
    div.textContent = `${r.nome} (${r.tipo}) - ${r.descricao}`

    if (cargo === "admin"){
      const btnRemover = document.createElement("button")
      btnRemover.textContent = "Remover"
      btnRemover.style.marginLeft = "10px"
      btnRemover.onclick = () => removerRecurso(r.id)
      div.appendChild(btnRemover)
    }
    lista.appendChild(div)
  })
}

async function adicionarRecurso(){
  const nome = document.getElementById("nome-recurso").value
  const tipo = document.getElementById("tipo-recurso").value
  const descricao = document.getElementById("descricao").value
  const token = localStorage.getItem("token")
  const res = await fetch("http://localhost:5000/recursos",{
    method: "POST",
    headers:{
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({ nome, tipo, descricao }),
  })

  if (res.ok){
    alert("Recurso adicionado com sucesso")
    location.reload()
  }
}

async function removerRecurso(id){
  const token = localStorage.getItem("token")
  if (!confirm("Tem certeza que deseja remover esse recurso?")) return

  const res = await fetch(`http://localhost:5000/recursos/${id}`, {
    method: "DELETE",
    headers: {
      Authorization: `Bearer ${token}`,
    },
  })

  if (res.ok){
    alert("Recurso removido com sucesso")
    location.reload()
  } else {
    alert("Erro ao remover recurso")
  }
}

if (location.pathname.includes("dashboard")){
  window.onload = carregarDashboard
}