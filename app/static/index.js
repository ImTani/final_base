// Function to schedule a notification at 9 PM
function scheduleNotificationAt9PM() {
    // Get the current date and time
    var now = new Date();

    // Calculate the time until 9 PM
    var timeUntil9PM = new Date(now.getFullYear(), now.getMonth(), now.getDate(), 18, 8, 0) - now;

    // If it's already past 9 PM, schedule the notification for the next day
    if (timeUntil9PM < 0) {
        timeUntil9PM += 24 * 60 * 60 * 1000; // Add 24 hours
    }

    // Schedule the notification
    setTimeout(function() {
        // Check if the browser supports notifications
        if (!("Notification" in window)) {
            console.log("This browser does not support system notifications");
        } else if (Notification.permission === "granted") {
            // If permission is already granted, show the notification
            showNotification();
        } else if (Notification.permission !== 'denied') {
            // Otherwise, request permission from the user
            Notification.requestPermission().then(function (permission) {
                if (permission === "granted") {
                    showNotification();
                }
            });
        }
    }, timeUntil9PM);
}

// Function to display the notification
function showNotification() {
    var notification = new Notification("Scheduled Notification", {
        body: "It's 9 PM!"
    });

    // Close the notification after 5 seconds
    setTimeout(notification.close.bind(notification), 5000);
}

// Call the function to schedule the notification
scheduleNotificationAt9PM();
