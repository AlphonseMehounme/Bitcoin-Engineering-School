document.addEventListener('DOMContentLoaded', function() {
    var card = $('#id_bsd');
    card.on('click', function() {
        window.location.href = '/login_besd';
    });

    $('#id_bsd2').on('click', function() {
	window.location.href = '/login_besd';
    });

    $('#id_home').on('click', function() {
	window.location.href = '/';
    });
    $('#join').on('click', function() {
        window.location.href = '/join';
    });

    $('#join2').on('click', function() {
	window.location.href = '/join';
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
    $('#verify111').on('click', function() {
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
		console.log(content);
		if (content == 2) {
			$("#status111").text("Validated");
			$("#status111").css('color', 'green');
		}
		else {
			$("#status111").text("Failed");
			$("#status111").css('color', 'red');
		}
            },
            error: function(xhr, status, error) {
                console.error(`Error fetching file: ${xhr.status} ${xhr.statusText}`);
            }
        });
    });

    $('#verify112').on('click', function() {
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
		console.log(content);
		if (content == 1) {
			$("#status112").text("Validated");
			$("#status112").css('color', 'green');
		}
		else {
			$("#status112").text("Failed");
			$("#status112").css('color', 'red')
		}
	    },
	    error: function(xhr, status, error) {
		console.error(`Error fetching file: ${xhr.status} ${xhr.statusText}`);
	    }
	});
    });
});
