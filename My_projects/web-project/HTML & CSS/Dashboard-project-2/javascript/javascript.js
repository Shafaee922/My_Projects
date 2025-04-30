var ctx1 = document.getElementById('myAreaChart1').getContext('2d');
    var myAreaChart1 = new Chart(ctx1, {
      type: 'line', // Line chart type
      data: {
        labels: ['January', 'February', 'March', 'April', 'May'], // X-axis labels
        datasets: [
          {
            label: 'Sales 1',
            data: [10, 20, 30, 25, 40], // Sales data for Sales 1
            fill: true,
            backgroundColor: 'rgba(75, 192, 192, 0.2)', // Light green background
            borderColor: 'rgba(75, 192, 192, 1)', // Green line
            borderWidth: 3,
            tension: 0.4, // Slightly curved lines
            pointRadius: 6, // Bigger points
            pointBackgroundColor: 'rgba(75, 192, 192, 1)', // Green points
            pointBorderColor: '#fff', // White border for points
            pointBorderWidth: 2
          },
          {
            label: 'Sales 2', // New dataset for Sales 2
            data: [15, 25, 35, 30, 50], // Sales data for Sales 2
            fill: true,
            backgroundColor: 'rgba(153, 102, 255, 0.2)', // Purple background
            borderColor: 'rgba(153, 102, 255, 1)', // Purple line
            borderWidth: 3,
            tension: 0.4, // Slightly curved lines
            pointRadius: 6, // Bigger points
            pointBackgroundColor: 'rgba(153, 102, 255, 1)', // Purple points
            pointBorderColor: '#fff', // White border for points
            pointBorderWidth: 2
          }
        ]
      },
      options: {
        responsive: true, // Makes the chart responsive
        maintainAspectRatio: false, // Allows the chart to resize with the container
        scales: {
          x: {
            beginAtZero: true, // Ensure x-axis starts at zero
            grid: {
              color: 'rgba(0, 0, 0, 0.1)', // Light grid lines for x-axis
            }
          },
          y: {
            beginAtZero: true, // Ensure y-axis starts at zero
            grid: {
              color: 'rgba(0, 0, 0, 0.1)', // Light grid lines for y-axis
            }
          }
        },
        plugins: {
          tooltip: {
            enabled: true,
            backgroundColor: 'rgba(0, 0, 0, 0.7)', // Tooltip background color
            titleColor: '#fff', // Tooltip title text color
            bodyColor: '#fff', // Tooltip body text color
            callbacks: {
              // Customizing the tooltip to show both the label and value in a better way
              label: function(tooltipItem) {
                return tooltipItem.dataset.label + ': ' + tooltipItem.raw + ' units';
              }
            }
          },
          legend: {
            position: 'top', // Positioning the legend at the top
            labels: {
              boxWidth: 20, // Size of the legend box
              font: {
                size: 14 // Increase legend font size
              }
            }
          }
        },
        animation: {
          duration: 1000, // Animation duration for rendering
          easing: 'easeOutBounce' // Animation easing function for a smoother effect
        }
      }
    });