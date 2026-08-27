<?php
/**
 * Master Page Template: Home (CodeIgniter View)
 */

// Render Header Template
require APPPATH . 'Views/templates/header.php';

// Render Navigation Bar
require APPPATH . 'Views/templates/navbar.php';

// Render Main Page Sections in Strategic Editorial Order
require APPPATH . 'Views/sections/hero.php';
require APPPATH . 'Views/sections/why_us.php';
require APPPATH . 'Views/sections/services.php';
require APPPATH . 'Views/sections/industries.php';
require APPPATH . 'Views/sections/technology.php';
require APPPATH . 'Views/sections/cpa_partner.php';
require APPPATH . 'Views/sections/process.php';
require APPPATH . 'Views/sections/about_lekhankan.php';
require APPPATH . 'Views/sections/team.php';
require APPPATH . 'Views/sections/contact.php';

// Render Footer Template
require APPPATH . 'Views/templates/footer.php';
