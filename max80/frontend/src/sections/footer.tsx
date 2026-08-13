import Logo from "../components/logo";
import { Logo_cids } from "../_cids";
import { Logo_styles } from "../_styles";
import { logos as logosContent } from "../content";
/** Site footer. */
export default function Footer({ logos = logosContent } = {}) {
  return (
    <footer className="border-t border-solid border-t-border flex pt-6 pb-10 px-4 flex-col items-center gap-13.5 bg-color-003" data-cid="n427">
      <div className="flex flex-col items-center gap-6" data-cid="n428">
        <p className="block text-color-001 font-semibold leading-6" data-cid="n429">
          {" Trusted By 50,000+ Customers Across The World "}
        </p>
        <div className="flex flex-wrap justify-center items-center gap-6" data-cid="n430">
          {logos.map((d, i) => <Logo key={i} d={d} cids={Logo_cids[i]} styles={Logo_styles[i]} />)}
        </div>
      </div>
      <div className="flex justify-center items-center gap-2 text-muted leading-6" data-cid="n442">
        <span className="block" data-cid="n443">
          Copyright © 2026 | SuperAGI.
        </span>
        <span className="block text-color-006" data-cid="n444">
          |
        </span>
        <span className="block" data-cid="n445">
          SuperAGI is a product of Contlo INC.
        </span>
        <span className="block text-color-006" data-cid="n446">
          |
        </span>
        <a className="block underline cursor-pointer hover:text-clr-5 hover:outline-clr-5 hover:[text-decoration-color:var(--clr-5)]" data-cid="n447" data-component="link" href="/terms">
          {" Terms of Usage "}
        </a>
        <span className="block text-color-006" data-cid="n448">
          |
        </span>
        <a className="block underline cursor-pointer hover:text-clr-5 hover:outline-clr-5 hover:[text-decoration-color:var(--clr-5)]" data-cid="n449" data-component="link" href="/privacy-policy">
          {" Privacy Policy "}
        </a>
        <span className="block text-color-006" data-cid="n450">
          |
        </span>
        <span className="block" data-cid="n451">
          Call us at +1 (302) 599-6365
        </span>
      </div>
    </footer>
  );
}
