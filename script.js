window.onload = function () {
    // Show only home section on load
    document.getElementById('home').style.display = 'block';
    ['donor', 'request', 'hospital', 'admin'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.style.display = 'none';
    });
};
function showSection(sectionId) {
    document.getElementById('home').style.display = 'none';

    ['donor', 'request', 'hospital', 'admin'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.style.display = (id === sectionId ? 'block' : 'none');
    });
}
const sections = ['donor', 'request', 'hospital', 'admin'];

function showSection(id) {
sections.forEach(sec => {
    document.getElementById(sec).classList.add('hidden');
});
document.getElementById(id).classList.remove('hidden');
document.getElementById(id).scrollIntoView({ behavior: 'smooth' });
}


// Navbar link behavior
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', function (e) {
        const href = this.getAttribute('href').substring(1);
        if (href !== 'admin') {
            e.preventDefault();
            showSection(href);
        }
    });
});
    window.onscroll = function () {
        document.getElementById("backToTopBtn").style.display = 
            (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) 
            ? "block" 
            : "none";
    };

    function scrollToTop() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function checkAdminPassword() {
    const password = prompt("Enter admin password:");
    if (password === "admin123") {
        showSection("admin");
    } else {
        alert("Incorrect password!");
    }
}

    async function submitForm(event, url, formId, method = 'POST') {
        event.preventDefault();
        const formData = new FormData(document.getElementById(formId));
        const jsonObject = {};
        formData.forEach((value, key) => jsonObject[key] = value);

        const response = await fetch(url, {
            method: method,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(jsonObject)
        });

        const result = await response.json();
        alert(result.message || result.error);
    }

    async function fetchData(endpoint) {
        try {
            const res = await fetch('http://localhost:5000' + endpoint);
            if (!res.ok) throw new Error("Failed to fetch data.");
            const data = await res.json();

            const container = document.getElementById("viewData");
            if (!Array.isArray(data) || data.length === 0) {
                container.innerHTML = "<p class='text-danger'>No data found.</p>";
                return;
            }

            const headers = Object.keys(data[0]);
            let tableHTML = `<table class="table table-bordered table-striped"><thead><tr>`;
            headers.forEach(header => {
                tableHTML += `<th>${header.replace(/_/g, ' ')}</th>`;
            });
            tableHTML += `</tr></thead><tbody>`;
            data.forEach(row => {
                tableHTML += `<tr>`;
                headers.forEach(header => {
                    tableHTML += `<td>${row[header]}</td>`;
                });
                tableHTML += `</tr>`;
            });
            tableHTML += `</tbody></table>`;
            container.innerHTML = tableHTML;
        } catch (error) {
            console.error(error);
            document.getElementById("viewData").innerHTML = `<p class='text-danger'>Error loading data.</p>`;
        }
    }

    // Attach form submission handlers
    document.getElementById('donorForm').addEventListener('submit', (e) => submitForm(e, 'http://localhost:5000/donors', 'donorForm'));
    document.getElementById('requestForm').addEventListener('submit', (e) => submitForm(e, 'http://localhost:5000/recipients', 'requestForm'));
    document.getElementById('hospitalForm').addEventListener('submit', (e) => submitForm(e, 'http://localhost:5000/hospitals', 'hospitalForm'));
    document.getElementById('bloodBankForm').addEventListener('submit', (e) => submitForm(e, 'http://localhost:5000/bloodbanks', 'bloodBankForm'));
    document.getElementById('inventoryForm').addEventListener('submit', (e) => submitForm(e, 'http://localhost:5000/bloodinventory', 'inventoryForm'));

    document.getElementById('upinventoryForm').addEventListener('submit', (e) => {
        const inventoryId = document.getElementById('inventoryId').value;
        submitForm(e, `http://localhost:5000/bloodinventory/${inventoryId}`, 'upinventoryForm', 'PUT');
    });

    document.getElementById('updateRecipientForm').addEventListener('submit', (e) => {
        const id = document.getElementById('updateRecipientId').value;
        submitForm(e, `http://localhost:5000/recipients/${id}`, 'updateRecipientForm', 'PUT');
    });