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


function initVehicleChart() {
    const ctx = document.getElementById('vehicleStatusChart').getContext('2d');
    const activeVehicles = document.body.getAttribute('data-active-vehicles');
    const inactiveVehicles = document.body.getAttribute('data-inactive-vehicles');
    console.log({activeVehicles})
    const vehicleStatusChart = new Chart(ctx, {
            type: 'pie',  // Choose chart type (pie, bar, line, etc.)
            data: {
                'labels': ['Active', 'Inactive'],
                'datasets': [{
                    'data': [activeVehicles, inactiveVehicles],
                    'backgroundColor': ['#008000', '#FF0000'],
                }]
            },  // Pass chart data from Python context
            options: {
                responsive: true, // Enable responsiveness
                title: 'Vehicle Status'
                // Add other chart options as needed (e.g., title, legend)
            }
        }
        );
    }

function initDriverChart() {
    const ctx = document.getElementById('driverStatusChart').getContext('2d');
    const assignedDrivers = document.body.getAttribute('data-assigned-drivers');
    const unassignedDrivers = document.body.getAttribute('data-unassigned-drivers');
    console.log({unassignedDrivers})
    const vehicleStatusChart = new Chart(ctx, {
            type: 'pie',  // Choose chart type (pie, bar, line, etc.)
            data: {
                'labels': ['Assigned', 'Unassigned'],
                'datasets': [{
                    'data': [assignedDrivers, unassignedDrivers],
                    'backgroundColor': ['#008000', '#FF0000'],
                }]
            },  // Pass chart data from Python context
            options: {
                responsive: true, // Enable responsiveness
                title: 'Driver Status'
                // Add other chart options as needed (e.g., title, legend)
            }
        }
        );
    }


window.onload = () => {
    initVehicleChart();
    initDriverChart();
};

