var poll_url = '/path/to/json';
var post_url = '/path/to/post';

function handle_data(data) {
    // handle...
}

function poll() {
    var poll_interval=10;

    $.ajax({
        url: poll_url,
        type: "GET",
        dataType: "json",
        success: function(data) {
            handle_data(data);
            poll_interval=10;
        },
        error: function () {
            poll_interval=10000;
        },
        complete: function () {
            setTimeout(poll, poll_interval);
        },
    });
}

function send() {
    $.ajax({
        url: post_url,
        type: "POST",
        dataType: 'json',
        data: {
            // data
        },
        complete: function () {
            // clear any forms
        },
    });
}

$(function() {
    // define how data is sent
    poll();
})