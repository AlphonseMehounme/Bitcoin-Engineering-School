document.addEventListener('DOMContentLoaded', function() {
    var card = document.getElementById('id_bsd');
    card.addEventListener('click', function() {
        window.location.href = '/login_besd';
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var card = document.getElementById('id_ld');
    card.addEventListener('click', function() {
        window.location.href = '/login_ld';
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var card = document.getElementById('desd_chapter_2');
    card.addEventListener('click', function() {
        window.location.href = '/login_besd_c2_l';
    });
});


document.addEventListener('DOMContentLoaded', function() {
    var card = document.getElementById('ld_c2');
    card.addEventListener('click', function() {
        window.location.href = '/login_ld_c2';
    });
});

document.addEventListener('DOMContentLoaded', function() {
    $('#verify1').on('click', function() {
        const owner = "alphonsemehounme";
        const repo = "bitdev";
        const path = "chapter1/anwser1.txt";
        const branch = "main";
        const url2 = 'https://api.github.com/repos/${owner}/${repo}/contents/${path}?ref=${branch}';
	const url = 'https://api.github.com/repos/alphonsemehounme/bitdev/contents/chapter1/answer1';

        $.ajax({
            url: url,
            method: "GET",
            headers: {
                "Accept": "application/vnd.github.v3+json"
            },
            success: function(response) {
                const content = atob(response.content);
		console.log(content)
                $("#status1").text($("#status1").val + ": validated");
            },
            error: function(xhr, status, error) {
                console.error(`Error fetching file: ${xhr.status} ${xhr.statusText}`);
            }
        });
    });
});
