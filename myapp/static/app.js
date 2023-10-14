
        function verifyDialog() {
            // Show the dialog box
            $("#dialog-box").css("display", "block");
            return false; // Prevent form submission
        }

        function closeDialog() {
            // Hide the dialog box
            $("#dialog-box").css("display", "none");
        }

        document.addEventListener('DOMContentLoaded', function() {
            verifyDialog();
        });