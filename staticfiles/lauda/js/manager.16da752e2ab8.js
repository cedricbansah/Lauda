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
                // Add other chart options as needed (e.g., title, legend)
            }
        }
        );
    }



window.onload = () => {
    initVehicleStatusChart();
    initVehicleTypeChart();
};

