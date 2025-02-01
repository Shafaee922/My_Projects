var ctx1 = document.getElementById('myAreaChart1').getContext('2d');
        var myAreaChart1 = new Chart(ctx1, {
            type: 'line',
            data: {
                labels: ['January', 'February', 'March', 'April', 'May'],
                datasets: [{
                    label: 'Sales 1',
                    data: [10, 20, 30, 25, 40],
                    fill: true,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 2,
                    tension: 0.4,
                    pointRadius: 5,
                    pointBackgroundColor: 'rgba(75, 192, 192, 1)',
                    pointBorderColor: '#fff',
                    pointBorderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        beginAtZero: true
                    },
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });




        var ctx = document.getElementById('myBarChart').getContext('2d');
        var myBarChart = new Chart(ctx, {
            type: 'bar', // Set chart type to 'bar'
            data: {
                labels: ['January', 'February', 'March', 'April', 'May'],
                datasets: [{
                    label: 'Sales',
                    data: [15, 18, 25, 30, 50], // Bar chart data
                    backgroundColor: 'rgba(153, 102, 255, 0.2)', // Bar color
                    borderColor: 'rgba(153, 102, 255, 1)', // Bar border color
                    borderWidth: 2 // Border width
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        beginAtZero: true // Ensure X-axis starts from 0
                    },
                    y: {
                        beginAtZero: true // Ensure Y-axis starts from 0
                    }
                }
            }
        });