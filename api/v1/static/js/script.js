document.addEventListener('DOMContentLoaded', function() {
    var card = $('#id_bsd');
    card.on('click', function() {
        window.location.href = '/login_besd';
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var card = $('#id_ld');
    card.on('click', function() {
        window.location.href = '/login_ld';
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var card = $('#desd_chapter_2');
    card.on('click', function() {
        window.location.href = '/login_besd_c2_l';
    });
});


document.addEventListener('DOMContentLoaded', function() {
    var card = $('#ld_c2');
    card.on('click', function() {
        window.location.href = '/login_ld_c2';
    });
});

document.addEventListener('DOMContentLoaded', function() {
    $('#verify1').on('click', function() {
        const owner = "alphonsemehounme";
	const url = `https://api.github.com/repos/${owner}/bitdev/contents/chapter1/answer1`;

        $.ajax({
            url: url,
            method: "GET",
            headers: {
                "Accept": "application/vnd.github.v3+json"
            },
            success: function(response) {
                const content = atob(response.content);
		console.log(content)
		if (content == False) {
			$("#status1").text("validated");
			$("#status1").css("color", "green")
		}
		else {
			$("#status1").text("Failed");
			$("#status1").css("color", "red")
		}
            },
            error: function(xhr, status, error) {
                console.error(`Error fetching file: ${xhr.status} ${xhr.statusText}`);
            }
        });
    });

    $('#verify2').on('click', function() {
	const owner = "alphonsemehounme";
	const url = `https://api.github.com/repos/${owner}/bitdev/contents/chapter1/answer2`;

	$.ajax({
	    url: url,
	    method: "GET",
	    headers: {
		"Accept": "application/vnd.github.v3+json"
	    },
	    success: function(response) {
		const content = atob(response.content);
		console.log(content)
		if (content == 1) {
			$("#status2").text("Validated")
			$("#status2").css("color", "green")
		}
		else {
			$("#status2").text("Failed")
			$("#status2").css("color", "red")
		}
	    },
	    error: function(xhr, status, error) {
		    console.error(`Error fetching file: ${xhr.status} ${xhr.statusText}`);
	    }
	});
    });
});
