
<!doctype html>
<html lang="en">
<head>
        
        <meta charset="utf-8" />
        <title>swift-bruss.com</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta content="Premium Multipurpose Admin & Dashboard Template" name="description" />
        <meta content="Themesbrand" name="author" />
        <!-- App favicon -->
        <link rel="shortcut icon" href="assets/images/favicon.ico">

        <!-- Bootstrap Css -->
        <link href="assets/css/bootstrap.min.css" id="bootstrap-style" rel="stylesheet" type="text/css" />
        <!-- Icons Css -->
        <link href="assets/css/icons.min.css" rel="stylesheet" type="text/css" />
        <!-- App Css-->
        <link href="assets/css/app.min.css" id="app-style" rel="stylesheet" type="text/css" />

        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        
        <script src="https://code.iconify.design/iconify-icon/1.0.2/iconify-icon.min.js"></script>

    </head>

    <body data-sidebar="dark" data-layout-mode="light">

    <!-- <body data-layout="horizontal" data-topbar="dark"> -->

        <!-- Begin page -->
        <div id="layout-wrapper">

            
            <header id="page-topbar">
                <div class="navbar-header">
                    <div class="d-flex">
                        <!-- LOGO -->
                        <div class="navbar-brand-box">
                            <a href="index.html" class="logo logo-dark">
                                <span class="logo-sm">
                                    <img src="assets/images/logo.svg" alt="" height="22">
                                </span>
                                <span class="logo-lg">
                                    <img src="assets/images/logo-dark.png" alt="" height="17">
                                </span>
                            </a>

                            <a href="index.html" class="logo logo-light">
                                <span class="logo-sm">
                                    <img src="https://swift-bruss.com/swift.png" alt="" height="22">
                                </span>
                                <span class="logo-lg">
                                    <img src="https://swift-bruss.com/swift.png" alt="" height="19">
                                </span>
                            </a>
                        </div>

                        <button type="button" class="btn btn-sm px-3 font-size-16 header-item waves-effect" id="vertical-menu-btn">
                            <i class="fa fa-fw fa-bars"></i>
                        </button>

                        
                    </div>

                    <div class="d-flex">

                        <div class="dropdown d-inline-block d-lg-none ms-2">
                            <button type="button" class="btn header-item noti-icon waves-effect" id="page-header-search-dropdown"
                            data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <b>USD</b>
                            </button>
                            
                        </div>

                        <div class="dropdown d-inline-block">
                            <div class="page-title-left">
                                        <ol class="breadcrumb m-0">
                                           <div class="dropdown">
                                                <button type="button" class="btn btn-light" data-bs-toggle="dropdown" aria-haspopup-right="true" aria-expanded="false">
                                                    <i class="mdi mdi-wallet me-2" style="float:right;"></i> 
                                                    <span class="d-none d-sm-inline-block">Account Balance 
                                                        <i class="mdi mdi-chevron-down"></i>
                                                    </span>
                                                </button>
                                                <div class="dropdown-menu dropdown-menu-end dropdown-menu-md">
                                                    <div class="dropdown-item-text">
                                                        <div>
                                                            <p class="text-muted mb-2">Available Balance</p>
                                                            <h5 class="mb-0">$0</h5>
                                                        </div>
                                                    </div>

                                                    <div class="dropdown-divider"></div>

                                                    <a class="dropdown-item" href="#">
                                                        Main Balance : <span class="float-end">$0</span>
                                                    </a>
                                                    <a class="dropdown-item" href="#">
                                                        Overdraft Balance : <span class="float-end">$0</span>
                                                    </a>

                                                    <div class="dropdown-divider"></div>

                                                     <a class="dropdown-item" href="inter-transfer">
                                                        Internal Transfer : <span class="float-end">Open</span>
                                                    </a>
                                                    <a class="dropdown-item" href="domestic-transfer">
                                                        Domestic Transfer : <span class="float-end">Open</span>
                                                    </a>
                                                    <a class="dropdown-item" href="international-transfer">
                                                        International Transfer : <span class="float-end">Open</span>
                                                    </a>

                                                </div>
                                            </div>
                                        </ol>
                                    </div>
                        </div>

                        
                        <div class="dropdown d-none d-lg-inline-block ms-1">
                            <button type="button" class="btn header-item noti-icon waves-effect" data-bs-toggle="fullscreen">
                                <i class="bx bx-fullscreen"></i>
                            </button>
                        </div>
                                                
                        <div class="dropdown d-inline-block">
                            <button type="button" class="btn header-item noti-icon waves-effect" id="page-header-notifications-dropdown"
                            data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <i class="bx bx-bell bx-tada"></i>
                                <span class="badge bg-danger rounded-pill">2</span>
                            </button>
                            <div class="dropdown-menu dropdown-menu-lg dropdown-menu-end p-0"
                                aria-labelledby="page-header-notifications-dropdown">
                                <div class="p-4">
                                    <div class="row align-items-center">
                                        <div class="col">
                                            <h6 class="m-0" key="t-notifications"> Notifications </h6>
                                        </div>
                                        <div class="col-auto">
                                            <a href="#!" class="small" key="t-view-all"> View All</a>
                                        </div>
                                    </div>
                                </div>
                                <div data-simplebar style="max-height: 250px;">

                                <a href='notification' class='text-reset notification-item'>
                                    <div class='d-flex'>
                                    <div class='avatar-xs me-2'>
                                        <span class='avatar-title bg-success rounded-circle font-size-16'>
                                            <i class='bx bx-bell'></i>
                                        </span>
                                    </div>
                                    <div class='flex-grow-1'>
                                        <h6 class='mb-1' key='t-shipped'>Loan Request</h6>
                                        <div class='font-size-6 text-muted'>
                                            <p class='mb-1' key='t-grammer'><small>Hello Ulysses P. Smith, Your request for a loan of $5000 has been submitted and under preview</small></p>
                                            <p class='mb-0'><i class='mdi mdi-clock-outline'></i> <span key='t-min-ago'> 2 hours ago</span></p>
                                        </div>
                                    </div>
                                   </div>
                                </a><a href='notification' class='text-reset notification-item'>
                                    <div class='d-flex'>
                                    <div class='avatar-xs me-2'>
                                        <span class='avatar-title bg-success rounded-circle font-size-16'>
                                            <i class='bx bx-bell'></i>
                                        </span>
                                    </div>
                                    <div class='flex-grow-1'>
                                        <h6 class='mb-1' key='t-shipped'>Transaction Pin Updated</h6>
                                        <div class='font-size-6 text-muted'>
                                            <p class='mb-1' key='t-grammer'><small>Hello Ulysses P. Smith, Your have successfully Updated your Transaction Pin, if you never perform this operation contact Support</small></p>
                                            <p class='mb-0'><i class='mdi mdi-clock-outline'></i> <span key='t-min-ago'> 2 hours ago</span></p>
                                        </div>
                                    </div>
                                   </div>
                                </a><a href='notification' class='text-reset notification-item'>
                                    <div class='d-flex'>
                                    <div class='avatar-xs me-2'>
                                        <span class='avatar-title bg-success rounded-circle font-size-16'>
                                            <i class='bx bx-bell'></i>
                                        </span>
                                    </div>
                                    <div class='flex-grow-1'>
                                        <h6 class='mb-1' key='t-shipped'>Account Created Successfully</h6>
                                        <div class='font-size-6 text-muted'>
                                            <p class='mb-1' key='t-grammer'><small>Hello Ulysses P. Smith, Thanks for Join Swift-bruss, Complete all verification to gain full access </small></p>
                                            <p class='mb-0'><i class='mdi mdi-clock-outline'></i> <span key='t-min-ago'> 3 hours ago</span></p>
                                        </div>
                                    </div>
                                   </div>
                                </a>                                    

                                 
                                </div>
                                <div class="p-2 border-top d-grid">
                                    <a class="btn btn-sm btn-link font-size-14 text-center" href="javascript:void(0)">
                                        <i class="mdi mdi-arrow-right-circle me-1"></i> <span key="t-view-more">View More..</span> 
                                    </a>
                                </div>
                            </div>
                        </div>

                        <div class="dropdown d-inline-block">
                            <button type="button" class="btn header-item waves-effect" id="page-header-user-dropdown"
                            data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <img class="rounded-circle header-profile-user" src="user_kyc/new.png"
                                    alt="Header Avatar">
                                <span class="d-none d-xl-inline-block ms-1" key="t-henry">ULYSSES P. SMITH</span>
                                <i class="mdi mdi-chevron-down d-none d-xl-inline-block"></i>
                            </button>
                            <div class="dropdown-menu dropdown-menu-end">
                                <!-- item-->
                                <a class="dropdown-item" href="profile"><i class="bx bx-user font-size-16 align-middle me-1"></i> <span key="t-profile">Profile</span></a>
                                <a class="dropdown-item" href="virtual_card"><i class="bx bx-credit-card-alt font-size-16 align-middle me-1"></i> <span key="bx bx-credit-card-alt">MY Card</span></a>
                                <a class="dropdown-item d-block" href="settings"><span class="badge bg-success float-end"></span><i class="bx bx-wrench font-size-16 align-middle me-1"></i> <span key="t-settings">Settings</span></a>
                                <!-- <a class="dropdown-item" href="#"><i class="bx bx-lock-open font-size-16 align-middle me-1"></i> <span key="t-lock-screen">Lock screen</span></a> -->
                                <div class="dropdown-divider"></div>
                                <a class="dropdown-item text-danger" id='logout_account'><i class="bx bx-power-off font-size-16 align-middle me-1 text-danger"></i> <span key="t-logout">Logout</span></a>
                            </div>
                        </div>

                        <div class="dropdown d-inline-block">
                            <button type="button" class="btn header-item noti-icon right-bar-toggle waves-effect">
                                <i class="bx bx-cog bx-spin"></i>
                            </button>
                        </div>

                    </div>
                </div>
            </header>

            <!-- ========== Left Sidebar Start ========== -->
            <div class="vertical-menu">

                <div data-simplebar class="h-100">

                    <!--- Sidemenu -->
                    <div id="sidebar-menu">
                        <!-- Left Menu Start -->
                        <ul class="metismenu list-unstyled" id="side-menu">
                            <li class="menu-title" key="t-menu">Menu</li>

                            <li>
                                <a href="index" class="has-arrow waves-effect">
                                    <i class="bx bx-home-circle"></i>
                                    <span key="t-dashboards">Dashboards</span>
                                </a>
                            </li>

                            <li>
                                <a href="javascript: void(0);" class="has-arrow waves-effect">
                                    <i class="bx bx-transfer"></i>
                                    <span key="t-layouts">Transfer</span>
                                </a>
                                <ul class="sub-menu" aria-expanded="true">
                                    <li>
                                      <a href="inter-transfer" class="waves-effect" key="t-vertical">Internal Transfer</a>
                                    </li>

                                    <li>
                                      <a href="domestic-transfer" class="waves-effect" key="t-vertical">Domestic Transfer</a>
                                    </li>

                                    <li>
                                      <a href="international-transfer" class="waves-effect" key="t-vertical">International Transfer</a>
                                    </li>
                                </ul>
                            </li>
                            
                            <li>
                                <a href="javascript: void(0);" class="has-arrow waves-effect">
                                    <i class="bx bx-transfer-alt"></i>
                                    <span key="t-layouts">Crypto Transfer</span>
                                </a>
                                <ul class="sub-menu" aria-expanded="true">
                                    <li>
                                      <a href="usdt-transfer" class="waves-effect" key="t-vertical">USDT Transfer</a>
                                    </li>
                                </ul>
                            </li>

                            
                            <li class="menu-title" key="t-apps">Apps</li>

                            <li>
                                <a href="profile" class="waves-effect">
                                    <i class="bx bx-user"></i>
                                    <span key="t-chat">My Profile</span>
                                </a>
                            </li>

                            <li>
                                <a href="settings" class="waves-effect">
                                    <i class="bx bx-wrench"></i>
                                    <span key="t-invoices">Account Settings</span>
                                </a>
                            </li>

                            <li>
                                <a href="javascript: void(0);" class="has-arrow waves-effect">
                                    <i class="bx bx-list-ol"></i>
                                    <span key="t-layouts">Transactions</span>
                                </a>
                                <ul class="sub-menu" aria-expanded="true">
                                    <li>
                                      <a href="transactions" class="waves-effect" key="t-vertical">Transactions</a>
                                    </li>

                                    <li>
                                      <a href="pending-transfer" class="waves-effect" key="t-vertical">Pending Transfer</a>
                                    </li>
                                </ul>
                            </li>

                            <li>
                                <a href="virtual_card" class="waves-effect">
                                    <i class="bx bx-credit-card-alt"></i>
                                    <span key="t-projects">My Card</span>
                                </a>
                            </li>

                            <li>
                                <a href="create_loan" class="waves-effect">
                                    <i class="bx bxl-mastercard"></i>
                                    <span key="t-contacts">LOAN Request</span>
                                </a>
                            </li>

                            <li>
                                 <a href="notification" class="dropdown-item text-danger">
                                    <i class="bx bx-bell bx-tada font-size-16 align-middle me-1 text-danger" >
                                    <span key="t-logout">Notifications <span class="badge bg-danger rounded-pill">2</span></span> </i> 
                                 </a>
                            </li>

                            <li>
                                 <a class="dropdown-item text-danger">
                                    <i class="bx bx-power-off font-size-16 align-middle me-1 text-danger" id='logout_account1'>
                                    <span key="t-logout">Logout</span> </i> 
                                 </a>
                            </li>

                        </ul>
                    </div>
                    <!-- Sidebar -->
                </div>
            </div>
            <!-- Left Sidebar End -->
<link rel="stylesheet" href="card1_style.css">
<link href="assets/libs/bootstrap-touchspin/jquery.bootstrap-touchspin.min.css" rel="stylesheet" type="text/css" />
         <div class="main-content">

                <div class="page-content">
                    <div class="container-fluid">

                        <!-- start page title -->
                        <div class="row">
                            <div class="col-12">
                                <div class="page-title-box d-sm-flex align-items-center justify-content-between">
                                    <h4 class="mb-sm-0 font-size-15">virtual Card<i class="bx bx-transfer">
                                    </i> </h4>

                                    <div class="page-title-right">
                                        <ol class="breadcrumb m-0">
                                        </ol>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="col-xl-12">
                                <div class="card" style="border-top-left-radius:30px; border-top-right-radius: 30px; ">
                                    
            <!----------Card Starts HERE------------>
                <div class="payment-title">
                    <h1>Virtual Card</h1>
                </div>
                    <div class="container preload">
                        <div class="creditcard">
                            <div class="front">
                                <div id="ccsingle"></div>
                   <svg version='1.1' id='cardfront' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'
                    x='0px' y='0px' viewBox='0 0 750 471' style='enable-background:new 0 0 750 471;' xml:space='preserve'>
                    <g id='Front'>
                        <g id='CardBackground'>
                            <g id='Page-1_1_'>
                                <g id='amex_1_'>
                                    <path id='Rectangle-1_1_' class='lightcolor grey' d='M40,0h670c22.1,0,40,17.9,40,40v391c0,22.1-17.9,40-40,40H40c-22.1,0-40-17.9-40-40V40
                            C0,17.9,17.9,0,40,0z' />
                                </g>
                            </g>
                            <g> <rect x='169.81' y='31.89' width='143.72' height='234.42' fill='#ff5f00'></rect> <path d='M317.05,197.6A149.5,149.5,0,0,1,373.79,80.39a149.1,149.1,0,1,0,0,234.42A149.5,149.5,0,0,1,317.05,197.6Z' transform='translate(-132.74 -48.5)' fill='#eb001b'></path> <path d='M615.26,197.6a148.95,148.95,0,0,1-241,117.21,149.43,149.43,0,0,0,0-234.42,148.95,148.95,0,0,1,241,117.21Z' transform='translate(-132.74 -48.5)' fill='#f79e1b'></path> </g>
                            <path class='darkcolor greydark' d='M750,431V193.2c-217.6-57.5-556.4-13.5-750,24.9V431c0,22.1,17.9,40,40,40h670C732.1,471,750,453.1,750,431z' />
                        </g>
                        <text transform='matrix(1 0 0 1 60.106 295.0121)' id='svgnumber' class='st2 st3 st4'>**** **** **** ****</text>
                        <text transform='matrix(1 0 0 1 54.1064 428.1723)' id='svgname' class='st2 st5 st6'>**MASTER CARD**</text>
                        <text transform='matrix(1 0 0 1 54.1074 389.8793)' class='st7 st5 st8'>Cardholder name</text>
                        <text transform='matrix(1 0 0 1 479.7754 388.8793)' class='st7 st5 st8'>expiration</text>
                        <text transform='matrix(1 0 0 1 65.1054 241.5)' class='st7 st5 st8'>card number</text>
                        <g>
                            <text transform='matrix(1 0 0 1 574.4219 433.8095)' id='svgexpire' class='st2 st5 st9'>0*/**</text>
                            <text transform='matrix(1 0 0 1 479.3848 417.0097)' class='st2 st10 st11'>VALID</text>
                            <text transform='matrix(1 0 0 1 479.3848 435.6762)' class='st2 st10 st11'>THRU</text>
                            <polygon class='st2' points='554.5,421 540.4,414.2 540.4,427.9' />
                        </g>
                        <g id='cchip'>
                            <g>
                                <path class='st2' d='M168.1,143.6H82.9c-10.2,0-18.5-8.3-18.5-18.5V74.9c0-10.2,8.3-18.5,18.5-18.5h85.3
                        c10.2,0,18.5,8.3,18.5,18.5v50.2C186.6,135.3,178.3,143.6,168.1,143.6z' />
                            </g>
                            <g>
                                <g>
                                    <rect x='82' y='70' class='st12' width='1.5' height='60' />
                                </g>
                                <g>
                                    <rect x='167.4' y='70' class='st12' width='1.5' height='60' />
                                </g>
                                <g>
                                    <path class='st12' d='M125.5,130.8c-10.2,0-18.5-8.3-18.5-18.5c0-4.6,1.7-8.9,4.7-12.3c-3-3.4-4.7-7.7-4.7-12.3
                            c0-10.2,8.3-18.5,18.5-18.5s18.5,8.3,18.5,18.5c0,4.6-1.7,8.9-4.7,12.3c3,3.4,4.7,7.7,4.7,12.3
                            C143.9,122.5,135.7,130.8,125.5,130.8z M125.5,70.8c-9.3,0-16.9,7.6-16.9,16.9c0,4.4,1.7,8.6,4.8,11.8l0.5,0.5l-0.5,0.5
                            c-3.1,3.2-4.8,7.4-4.8,11.8c0,9.3,7.6,16.9,16.9,16.9s16.9-7.6,16.9-16.9c0-4.4-1.7-8.6-4.8-11.8l-0.5-0.5l0.5-0.5
                            c3.1-3.2,4.8-7.4,4.8-11.8C142.4,78.4,134.8,70.8,125.5,70.8z' />
                                </g>
                                <g>
                                    <rect x='82.8' y='82.1' class='st12' width='25.8' height='1.5' />
                                </g>
                                <g>
                                    <rect x='82.8' y='117.9' class='st12' width='26.1' height='1.5' />
                                </g>
                                <g>
                                    <rect x='142.4' y='82.1' class='st12' width='25.8' height='1.5' />
                                </g>
                                <g>
                                    <rect x='142' y='117.9' class='st12' width='26.2' height='1.5' />
                                </g>
                            </g>
                        </g>
                    </g>
                    <g id='Back'>
                    </g>
                </svg>
            </div>
        </div>
    </div>
    <!---------Card ENDs Here------------->
                            <div class="col-xl-12">
                                <div class="card">
                                    <div class="card-body">
                                        <h4 class="card-title mb-4">
                                             <!-- <p class="response"></p> -->
                                        </h4>
                                        <p><center><font color='#ed0202'>Purchase a virtual Master card **</font></center></p>
                                                                                <form id="card_form" method="POST">
                                        	<div class="row mb-4">
                                                <label for="horizontal-firstname-input" class="col-sm-3 col-form-label">Payment System</label>
                                                <div class="col-sm-9">
                                                  <select class="form-control" id="pay_system" name="pay_system">
                                                  	<option value="">Select</option>
                                                    <option value="bank">Bank Transfer</option>
                                                    <option value="usdt">USDT</option>
                                                    <option value="btc">BITCOIN</option>
                                                  </select>
                                                </div>
                                            </div>

                                             <div class="row mb-4">
                                                <label for="" class="col-sm-3 col-form-label">Amount</label>
                                                <div class="col-sm-9">
                                                  <input type="number" class="form-control" type="card_amount" id='card_amount' name="card_amount" value="3000" aria-label="Amount (to the nearest dollar)" readonly="">
                                                </div>
                                            </div>

                                            <div class="row justify-content-end">
                                                <div class="col-sm-9">
                                                    <div>
                                                        <button id="send_pin" onclick='send(this)' class="btn btn-primary btn-rounded waves-effect waves-light" type="submit">Send</button>
                                                    </div>
                                                </div>
                                            </div>
                                        </form>
                                                                            </div>
                                    <p class="response"></p>
                                    <!-- end card body -->
                                </div>
                                <!-- end card -->
                            </div>
                        </div>
                    </div>


<script src="assets/js/jquery-3.4.1.min.js"></script>
<script>
  function send(id){
    // $("#myModal").modal('show');
    id.innerHTML = "Please wait..<div class='spinner-border spinner-border-sm' role='status'><span class='sr-only'>Loading...</span></div>";
    setTimeout(function(){
      id.innerHTML = "Send";
      // $("#myModal").modal('hide');
      window.scrollTo(0, 530);
     }, 3000);
    }
</script>

<center>
<div id="myModal" class="modal fade" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog" style="margin-top:180px; padding:-73px;">
        <div class="modal-content" style="background-color:#31202000; border: 1px solid rgba(0, 0, 0, 0);">
            <div class="modal-body">
                <img src="loader1.gif" width="50px">
            </div>
        </div>
    </div>
</div>
</center>

<script src="assets/libs/bootstrap-touchspin/jquery.bootstrap-touchspin.min.js"></script>
<div class="position-fixed top-0 end-0 p-2" style="z-index: 1005">
    <div id="ErrorToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
        <div class="toast-header">
            <img src="https://swift-bruss.com/swift.png" alt="" class="me-2" height="18">
            <strong class="me-auto">Error</strong>
            <small>Now..</small>
            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
        <div class="toast-body" style="background-color:red;">
            
        </div>
    </div>
</div>

<script src='https://unpkg.com/sweetalert/dist/sweetalert.min.js'></script>
 <script>
 $(document).ready(function(){
                $('#card_form').on('submit', function(e){
                    e.preventDefault();

                    var pay_system = $('#pay_system').val();
                    var card_amount = $('#card_amount').val();
                    
                    if(pay_system=="" ||  card_amount==""){
                       $(".toast-body").html('Input Required Field');
                       $("#ErrorToast").toast("show");
                       return false;
                    }

                    if(card_amount<3000) {
                      $(".toast-body").html('Error Try again');
                      $("#ErrorToast").toast("show");
                      $("#card_amount").val('3000');
                       return false;
                    }

                    if(pay_system=='bank') {
                      $(".toast-body").html('Bank Payment Not available at this moment');
                      $("#ErrorToast").toast("show");
                      $("#card_amount").val('3000');
                       return false;
                    }

                   
                     $.ajax({
                        type: "POST",
                        url: 'process/card.php',
                        data:{pay_system:pay_system, card_amount:card_amount},
                        dataType:"json",
                        success: function(data){
                           $(".response").html(data.content);
                           if(data.content=='successful'){
                              $(".response").html(data.content);
                             }else
                           if(data.content=='Error'){
                              $(".response").html(data.content);
                            }
                        },
                        error: function(data, errorThrown){
                        swal('Error', 'Network anormaly', 'error',{closeOnClickOutside: false,});
                       }
                    });
                    
                });
            });
</script>
<footer class="footer">
                    <div class="container-fluid">
                        <div class="row">
                            <p class="logout"></p>
                            <div class="col-sm-6">
                                <script>document.write(new Date().getFullYear())</script> © SWIFT-BRUSS                            </div>
                            <div class="col-sm-6">
                                <div class="text-sm-end d-none d-sm-block">
                                    Design & Develop by Swift-bruss                                </div>
                            </div>
                        </div>
                    </div>
                </footer>
            </div>
            <!-- end main content-->

        </div>
        <!-- END layout-wrapper -->

        <!-- Right Sidebar -->
        <div class="right-bar">
            <div data-simplebar class="h-100">
                <div class="rightbar-title d-flex align-items-center px-3 py-4">
            
                    <h5 class="m-0 me-2">Settings</h5>

                    <a href="javascript:void(0);" class="right-bar-toggle ms-auto">
                        <i class="mdi mdi-close noti-icon"></i>
                    </a>
                </div>

                <!-- Settings -->
                <hr class="mt-0" />
                <h6 class="text-center mb-0">Choose Layouts</h6>

                <div class="p-4">
                    <!-- <div class="mb-2">
                        <img src="assets/images/layouts/layout-1.jpg" class="img-thumbnail" alt="layout images">
                    </div> -->

                    <div class="form-check form-switch mb-3">
                        <input class="form-check-input theme-choice" type="checkbox" id="light-mode-switch" checked>
                        <label class="form-check-label" for="light-mode-switch">Use Light Mode</label>
                    </div>
    
                    <!-- <div class="mb-2">
                        <img src="assets/images/layouts/layout-2.jpg" class="img-thumbnail" alt="layout images">
                    </div> -->
                    <div class="form-check form-switch mb-3">
                        <input class="form-check-input theme-choice" type="checkbox" id="dark-mode-switch">
                        <label class="form-check-label" for="dark-mode-switch">Use Dark Mode</label>
                    </div>
    
                </div>

            </div> 
            <!-- end slimscroll-menu-->
        </div>
        <!-- /Right-bar -->

        <!-- Right bar overlay-->
        <div class="rightbar-overlay"></div>

        <!-- JAVASCRIPT -->
        <script src="assets/libs/jquery/jquery.min.js"></script>
        <script src="assets/libs/bootstrap/js/bootstrap.bundle.min.js"></script>
        <script src="assets/libs/metismenu/metisMenu.min.js"></script>
        <script src="assets/libs/simplebar/simplebar.min.js"></script>
        <script src="assets/libs/node-waves/waves.min.js"></script>

        <!-- apexcharts -->
        <script src="assets/libs/apexcharts/apexcharts.min.js"></script>

        <!-- dashboard init -->
        <script src="assets/js/pages/dashboard.init.js"></script>

        <!-- Bootstrap Toasts Js -->
        <script src="assets/js/pages/bootstrap-toastr.init.js"></script>

        <!-- App js -->
        <script src="assets/js/app.js"></script>
    </body>
</html>
<script src="//cdn.jsdelivr.net/npm/sweetalert2@11"></script>
<script>
$('#logout_account, #logout_account1').click(function() {
    $.ajax({
            type: 'POST',
            url: 'process/logout.php',
            dataType:'json',
            success: function(data){
                $('.logout').html(data.content);
               if(data.content=='Successful'){
                  $('.logout').html(data.content);
                 }else
               if(data.content=='Error'){
                 $('.logout').html(data.content);
                }
            },
            error: function(data, errorThrown){
              Swal.fire('The Internet?','Check network connection!','question');
               return false;
           }
         });
     });


$("#someDiv").hide();
setInterval(function(){
     $( "#someDiv" ).fadeIn(1000).fadeOut(2500);
},0)
</script>
<script src="//code.tidio.co/8bjfdyknbcqnyhbolnkfmizeukkm85pa.js" async></script>