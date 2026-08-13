/** Hero section — the page's lead block. */
export default function HeroSection() {
  return (
    <div className="flex p-20 flex-col items-center gap-2 max-md:p-6" data-cid="n35">
      <h1 className="block text-color-001 text-3xl font-bold leading-9" data-cid="n36" data-component="heading">
        Get Work done with SuperAGI
      </h1>
      <p className="block text-muted-foreground leading-6" data-cid="n37">
        {" Supercharge your business with digital workers and agentic software "}
      </p>
      <div className="h-[5.6875rem] flex mt-2 justify-center w-full" data-cid="n38" id="text-input">
        <div className="w-2/3 border border-solid border-color-002 flex relative py-2 px-3 rounded-xl flex-col self-stretch gap-2 [word-break:break-word] cursor-default max-md:w-full" data-cid="n39">
          <div className="block" data-cid="n40">
            <textarea className="w-full h-8 min-h-8 inline-block relative max-w-full rounded-md overflow-auto align-bottom text-color-001 text-sm leading-5.5 whitespace-pre-wrap cursor-text" data-cid="n41" data-component="textarea" id="homepage-chat-input" placeholder="What do you want to do?" value="" />
          </div>
          <div className="flex justify-end" data-cid="n42">
            <button className="h-8.5 border border-solid border-border flex relative py-1 pr-2 pl-1 rounded-lg justify-center items-center gap-1 text-background text-sm font-semibold leading-[1.0625rem] text-center whitespace-nowrap text-nowrap bg-clr-0 shadow-[var(--color-003)_0px_2px_0px_0px] cursor-pointer hover:bg-clr-2 hover:bg-[linear-gradient(0deg,_var(--clr-3)_0%,_var(--clr-3)_100%),_none] hover:[background-position:0%_0%,_0%_0%]" data-cid="n43" data-component="button" type="button">
              <img className="w-5 h-5 block max-w-full ml-1 overflow-clip align-middle" data-cid="n44" data-component="image" alt="send_icon" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
