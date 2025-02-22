$(document).ready(function () {
    // Simplified sidebar toggle
    $('#toggle-sidebar').on('click', function () {
        $('#sidebar').toggleClass('sidebar-collapsed');
        $('#main-content').toggleClass('sidebar-open');

        // Change icon based on state
        if ($('#sidebar').hasClass('sidebar-collapsed')) {
            $(this).html('<i class="fas fa-chevron-right"></i>');
        } else {
            $(this).html('<i class="fas fa-bars"></i>');
        }
    });

    // Topic expanding
    $('.topic-item').on('click', function (e) {
        // Don't expand if clicking on action buttons
        if ($(e.target).closest('a').length > 0) {
            return;
        }

        const topicId = $(this).data('topic-id');
        const entriesList = $(`#topic-entries-${topicId}`);
        const chevron = $(this).find('.fa-chevron-right');

        entriesList.toggleClass('open');
        chevron.toggleClass('rotate-90');
        $(this).toggleClass('active');
    });

    // Apply smooth hover effects to entries
    $('.entry-item, .topic-item').hover(
        function () { $(this).addClass('shadow-sm'); },
        function () { $(this).removeClass('shadow-sm'); }
    );

    // Add confirmation for delete actions
    $('a[href*="delete"]').on('click', function (e) {
        if (!confirm('Are you sure you want to delete this item? This cannot be undone.')) {
            e.preventDefault();
        }
    });

    // Auto-expand topic if viewing related entries
    {% if topic_id %}
    const currentTopicItem = $(`.topic-item[data-topic-id="{{ topic_id }}"]`);
    if (currentTopicItem.length > 0) {
        currentTopicItem.click();
        currentTopicItem.addClass('bg-orange-100');
    }
    {% endif %}

    // Check if sidebar should be collapsed on mobile by default
    if (window.innerWidth < 768) {
        $('#toggle-sidebar').click();
    }
});
