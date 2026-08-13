/** Top navigation bar. */
export default function Navbar() {
  return (
    <nav className="h-12 flex justify-between items-center text-color-004 w-full" data-cid="n4" data-component="nav" id="homepage_navbar">
      <a className="h-15 flex py-4 pr-4 pl-3 justify-center cursor-pointer" data-cid="n5" data-component="link" aria-current="page" href="/">
        <img className="block max-w-full overflow-clip align-middle w-10 h-7" data-cid="n6" data-component="image" alt="SuperAGI - AI Super App for Work" id="superagi_logo" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" />
      </a>
      <div className="h-8.5 flex items-center" data-cid="n7">
        <button className="h-8.5 border border-solid border-border flex relative mr-2 py-1 px-5 rounded-[30px] justify-center items-center gap-1 text-background text-sm font-semibold leading-[1.0625rem] text-center whitespace-nowrap text-nowrap bg-clr-0 shadow-[var(--color-003)_0px_2px_0px_0px] cursor-pointer hover:bg-clr-2 hover:bg-[linear-gradient(0deg,_var(--clr-3)_0%,_var(--clr-3)_100%),_none] hover:[background-position:0%_0%,_0%_0%]" data-cid="n8" data-component="button" type="button">
          <img className="w-4 h-4 block max-w-full overflow-clip align-middle" data-cid="n9" data-component="image" alt="bolt" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" />
          <span className="block" data-cid="n10">
            Sign up for free
          </span>
        </button>
      </div>
    </nav>
  );
}
