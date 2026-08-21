<?php
/**
 * Master Page Template: Home (CodeIgniter View)
 */

// Render Header
require APPPATH . 'Views/templates/header.php';

// Render Navigation Bar
require APPPATH . 'Views/templates/navbar.php';

// Render Main Page Sections in Strategic Sequence
require APPPATH . 'Views/sections/hero.php';
require APPPATH . 'Views/sections/brand_story.php';
require APPPATH . 'Views/sections/why_us.php';
require APPPATH . 'Views/sections/services.php';
require APPPATH . 'Views/sections/industries.php';
require APPPATH . 'Views/sections/cpa_partner.php';
require APPPATH . 'Views/sections/process.php';
require APPPATH . 'Views/sections/team.php';
require APPPATH . 'Views/sections/lead_magnets.php';
require APPPATH . 'Views/sections/contact.php';

// Render Footer
require APPPATH . 'Views/templates/footer.php';
