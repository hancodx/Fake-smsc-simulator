async function loadMessages() {

    const response = await fetch("/messages");

    const messages = await response.json();

    const table = document.getElementById("messagesTable");

    table.innerHTML = "";

    messages.forEach(msg => {

        let statusClass = "";

        if (msg.status === "DELIVERED") {
            statusClass = "status-delivered";
        }

        else if (msg.status === "FAILED") {
            statusClass = "status-failed";
        }

        else {
            statusClass = "status-pending";
        }

        table.innerHTML += `
            <tr>
                <td>${msg.id}</td>
                <td>${msg.to}</td>
                <td>${msg.priority}</td>
                <td class="${statusClass}">
                    ${msg.status}
                </td>
                <td>${msg.latency} ms</td>
                <td>${msg.campaignId}</td>
                <td>${msg.createdAt}</td>
            </tr>
        `;
    });
}


async function loadStats() {

    const response = await fetch("/stats");

    const stats = await response.json();

    document.getElementById("total").innerText =
        stats.total;

    document.getElementById("delivered").innerText =
        stats.delivered;

    document.getElementById("failed").innerText =
        stats.failed;

    document.getElementById("pending").innerText =
        stats.pending;
}


function refreshDashboard() {
    loadMessages();
    loadStats();
}


setInterval(refreshDashboard, 1000);

refreshDashboard();