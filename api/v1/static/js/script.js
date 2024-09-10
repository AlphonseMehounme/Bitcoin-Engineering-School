/*------------------*\
 * Main JS File
\*------------------*/

/* Handle Main button click after Dom content load */
document.addEventListener('DOMContentLoaded', function() {
    $('#id_bsd').on('click', function() {
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

    $('#id_ld').on('click', function() {
        window.location.href = '/login_ld';
    });

    $('#desd_chapter_2').on('click', function() {
        window.location.href = '/login_besd_c2_l';
    });

    $('#ld_c2').on('click', function() {
        window.location.href = '/login_ld_c2';
    });

    $('#id_lnbcp').on('click', function() {
	window.location.href = '/login_lnbcp';
    });

    $('#lnbcp_chapter_2').on('click', function() {
	window.location.href = '/lnbcp2';
    });

    $('#lnbcp_chapter_3').on('click', function() {
	window.location.href = '/lnbcp3';
    });

    $('#lnbcp_chapter_4').on('click', function() {
	window.location.href = '/lnbcp4';
    });
	$gols2 = $('#goalslnbcp2');
	$res2 = $('#ressourceslnbcp2');
        $gols3 = $('#goalslnbcp3');
	$res3 = $('#ressourceslnbcp3');
	$gols4 = $('#goalslnbcp4');
	$res4 = $('#ressourceslnbcp4');
	$.ajax({
	    url: 'http://bes.alphonsemehounme.tech/api/v1/courses/f6aed2d0-bf16-4fbd-bcab-ef89f3174a4c',
	    method: "GET",
	    success: function(course) {

		let goals = course.chapters[0].Goals;
		$.each(goals, function(i, gola) {
		    $('#goalslnbcp1').append('<li>' + gola + '</li>');
		});
		
		let ressources = course.chapters[0].Ressources;
		$.each(ressources, function(i, ressource) {
		    $('#ressourceslnbcp1').append('<li>' + ressource + '</li>');
		});

		goals = course.chapters[1].Goals;
		$.each(goals, function(i, gola) {
		    $gols2.append('<li>' + gola + '</li>');
		});

		ressources = course.chapters[1].Ressources;
		$.each(ressources, function(i, ressource) {
		    $res2.append('<li>' + ressource + '</li>')
		});

		goals = course.chapters[2].Goals;
		$.each(goals, function(i, gola) {
		    $gols3.append('<li>' + gola + '</li>');
		});

		ressources = course.chapters[2].Ressources;
		$.each(ressources, function(i, ressource) {
		    $res3.append('<li>' + ressource + '</li>');
		});

		goals = course.chapters[3].Goals;
		$.each(goals, function(i, gola) {
		    $gols4.append('<li>' + gola + '</li>');
		});

		ressources = course.chapters[3].Ressources;
		$.each(ressources, function(i, ressource) {
		    $res4.append('<li>' + ressource + '</li>');
		});
	    },
	    error: function(xhr, status, error) {
		console.error(`Error fetching file: ${xhr.status} ${xhr.statusText}`)
	    }
	});


});

/* Handle code checks */
document.addEventListener('DOMContentLoaded', function() {
    /* Fetch content from user repo and compare for check */
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

    /* Fetch content from user repo and compare for check */
    $('#verify112').on('click', function() {
	//console.log({{ session.github_username }});
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
