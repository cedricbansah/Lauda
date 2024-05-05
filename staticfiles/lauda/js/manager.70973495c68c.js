// Function to switch between tabs
function openTab(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

// Open default tab on page load
document.getElementById("defaultOpen").click();


function initVehicleStatusChart() {
    const ctx = document.getElementById('vehicleStatusChart').getContext('2d');
    const activeVehicles = document.body.getAttribute('data-active-vehicles');
    const inactiveVehicles = document.body.getAttribute('data-inactive-vehicles');
    console.log({activeVehicles})
    const vehicleStatusChart = new Chart(ctx, {
            type: 'doughnut',  // Choose chart type (pie, bar, line, etc.)
            data: {
                'labels': ['Active', 'Inactive'],
                'datasets': [{
                    'data': [activeVehicles, inactiveVehicles],
                    'backgroundColor': ['#008000', '#FF0000'],
                }]
            },  // Pass chart data from Python context
            options: {
                layout: {
                    padding: 20
                },
                responsive: true, // Enable responsiveness
                title: 'Vehicle Status'
                // Add other chart options as needed (e.g., title, legend)
            }
        }
        );
    }

function initVehicleTypeChart() {
    const ctx = document.getElementById('vehicleTypeChart').getContext('2d');
    const sedanCount = document.body.getAttribute('data-sedan-count');
    const suvCount = document.body.getAttribute('data-suv-count');
    const minivanCount = document.body.getAttribute('data-minivan-count');
    const pickupTruckCount = document.body.getAttribute('data-pickuptruck-count');
    const hatchbackCount = document.body.getAttribute('data-hatchback-count');
    console.log({pickupTruckCount})
    const vehicleTypeChart = new Chart(ctx, {
            type: 'doughnut',  // Choose chart type (pie, bar, line, etc.)
            data: {
                'labels': ['Sedans', 'Suvs', 'Pick-up Trucks','Minivans', 'Hatchbacks'],
                'datasets': [{
                    'data': [sedanCount, suvCount, minivanCount, pickupTruckCount, hatchbackCount],
                    'backgroundColor': ['#008000', '#FF0000', '#bfbd21', '#bf21af', '#21bfb7'],
                }]
            },  // Pass chart data from Python context
            options: {
                responsive: true, // Enable responsiveness
                title: 'Vehicle Type'

            }
        }
        );
    }



// Pagination variables for driver table
const driversPerPage = 10;
const allDrivers = JSON.parse('{{ all_drivers_json|escapejs }}')
const startIndex = (currentPage -1) * driversPerPage;

console.log(allDrivers)

// Function to display drivers for current page
function displayDriversPerPage() {
    // const startIndex = (currentPage -1) * driversPerPage;
    const endIndex = startIndex + driversPerPage;
    const driversForPage = allDrivers.slice(startIndex, endIndex);

    const tableBody = document.getElementById('driver-table-body');
    tableBody.innerHTML = '';

    driversForPage.forEach(driver => {
        const row = document.createElement('tr');
        row.innerHTML = `
        <td>{{ driver.first_name }}</td>
        <td>{{ driver.last_name }}</td>
        <td>{{ driver.email }}</td>
        <td>{{ driver.phone_number }}</td>
        <td>{{ driver.date_of_birth }}</td>
        <td>{{ driver.address }}</td>
        <td>{{ driver.license_number }}</td>
        `;
        tableBody.appendChild(row);
    })
}

// Event Listener for next page button
document.getElementById('next-page-btn').addEventListener('click', () => {
    if (currentPage < totalPages) {
        currentPage++;
        displayDriversPerPage()
    }
});

// Event listener for previous page button
document.getElementById('prev-page-btn').addEventListener('click', () => {
    if (currentPage > 1) {
        currentPage--;
        displayDriversPerPage();
    }
});



let currentPage = 1;
const vehiclesPerPage = 10;
const allVehicles = JSON.parse('{{ all_vehicles_json|escapejs }}')
console.log(allVehicles)


// Function to display drivers for current page
function displayVehiclesPerPage() {
    const startIndex = (currentPage -1) * vehiclesPerPage;
    const endIndex = startIndex + vehiclesPerPage;
    const vehiclesForPage = allVehicles.slice(startIndex, endIndex);

    const tableBody = document.getElementById('vehicle-table-body');
    tableBody.innerHTML = '';

    vehiclesForPage.forEach(driver => {
        const row = document.createElement('tr');
        row.innerHTML = `
        <td>{{ vehicle.year }}</td>
        <td>{{ vehicle.make }}</td>
        <td>{{ vehicle.model }}</td>
        <td>{{ vehicle.color }}</td>
        <td>{{ vehicle.license_plate }}</td>
        <td>{{ vehicle.vehicle_type }}</td>
        <td>{{ vehicle.vehicle_status }}</td>
        <td>{{ vehicle.driver_assigned }}</td>
        `;
        tableBody.appendChild(row);
    })
}

// Event Listener for next page button
document.getElementById('next-page-btn').addEventListener('click', () => {
    if (currentPage < totalPages) {
        currentPage++;
        displayVehiclesPerPage()
    }
});

// Event listener for previous page button
document.getElementById('prev-page-btn').addEventListener('click', () => {
    if (currentPage > 1) {
        currentPage--;
        displayVehiclesPerPage();
    }
});

window.onload = () => {
    initVehicleStatusChart();
    initVehicleTypeChart();
    displayDriversPerPage();
    displayVehiclesPerPage();
};