<?php
namespace Config;

/**
 * CodeIgniter Route Definitions
 */
class Routes {
    public static array $routes = [
        'GET' => [
            '/' => 'Home::index',
            'home' => 'Home::index',
            'about' => 'Home::index#about',
            'services' => 'Home::index#services',
            'why-us' => 'Home::index#why-us',
            'industries' => 'Home::index#industries',
            'process' => 'Home::index#process',
            'contact' => 'Home::index#contact'
        ],
        'POST' => [
            'contact/submit' => 'Home::submitContact'
        ]
    ];
}
