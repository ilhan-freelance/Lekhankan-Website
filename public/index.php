<?php
/**
 * CodeIgniter 4 Front Controller Entry Point (Public Web Root)
 */

define('ROOTPATH', realpath(__DIR__ . '/../') . '/');
define('APPPATH', ROOTPATH . 'app/');
define('WRITABLEPATH', ROOTPATH . 'writable/');

// Load CodeIgniter Helpers & Core Configuration
require_once APPPATH . 'Helpers/url_helper.php';
require_once APPPATH . 'Config/App.php';
require_once APPPATH . 'Config/Routes.php';
require_once APPPATH . 'Controllers/Home.php';

// Dispatch Request to Controller
$controller = new \App\Controllers\Home();

$requestUri = parse_url($_SERVER['REQUEST_URI'] ?? '/', PHP_URL_PATH);
$requestMethod = $_SERVER['REQUEST_METHOD'] ?? 'GET';

if ($requestMethod === 'POST' && strpos($requestUri, 'contact/submit') !== false) {
    $controller->submitContact();
} else {
    $controller->index();
}
