$('#sort-selector').change(function() {
    var selector = $(this);
    var currentUrl = new URL(window.location);
    var selectedVal = selector.val();

    if(selectedVal != "reset"){
        var sort = selectedVal.split("_")[0];
        var direction = selectedVal.split("_")[1];
        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);
        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");
        window.location.replace(currentUrl);
    }
})

/** Function to toggle a reply in comments thread and ensure empty reply text area | Adapted from Mimir's Index | https://github.com/edchalk96/mimirs_index/ */

function toggleReply(id) {
    const replyForm = document.getElementById('reply-' + id);
    replyForm.classList.toggle('d-none');

    if (!replyForm.classList.contains('d-none')) {
        const replyTextArea = replyForm.querySelector('textarea');
        if (replyTextArea) {
            replyTextArea.value = '';
        }
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const editButtons = document.getElementsByClassName("edit-btn");
    const commentForm = document.getElementById("commentForm");
    const commentText = commentForm ? commentForm.querySelector("textarea") : null;

    const submitButton = document.getElementById("submitButton");
    const commentHeading = document.getElementById("commentHeading");

    const deleteModal = new bootstrap.Modal(document.getElementById("deleteCommentModal"));
    const deleteButtons = document.getElementsByClassName("comment-delete-btn");
    const deleteConfirm = document.getElementById("deleteConfirm");

    /** Functionality to edit comments */

    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.currentTarget.getAttribute("data-comment_id");

            let bodyElement = document.getElementById(`body-${commentId}`);
            if (!bodyElement) return;

            let commentContent = bodyElement.innerText.trim();

            if (commentText) {
                commentText.value = commentContent;
            }

            submitButton.innerText = "Update";
            commentHeading.innerText = "Update Comment";
            commentForm.setAttribute("action", `edit_comment/${commentId}`);
            commentForm.scrollIntoView({ behavior: 'smooth' });
        });
    }

    /** Functionality for deletion of comments */
    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.currentTarget.getAttribute("comment_id");
            deleteConfirm.href = `delete_comment/${commentId}`;
            deleteModal.show();
        });
    }

    const addIdeaModal = document.getElementById('addIdeaModal');
    if (addIdeaModal) {
        $(addIdeaModal).on('shown.bs.modal', function () {
            $(addIdeaModal).find('select.django-select2').each(function () {
                const $select = $(this);

                // Re-parent the dropdown container to the modal so it isn't hidden behind it
                if ($select.hasClass('select2-hidden-accessible')) {
                    $select.data('select2').$dropdown.appendTo($(addIdeaModal));
                } else {
                    // Fallback if djangoSelect2 hasn't fanned out yet
                    if (typeof $.fn.djangoSelect2 === 'function') {
                        $select.djangoSelect2({
                            dropdownParent: $(addIdeaModal),
                            width: '100%'
                        });
                    }
                }
            });
        });
    }
});