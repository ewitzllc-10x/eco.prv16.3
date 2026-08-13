import type { CardLink2Styles } from "../_styles";
import { cn } from "../../lib/utils";
export type CardLink2Data = {
  href: string;
  alt: string;
  imgSrc: string;
  title: string;
  description: string;
};
/** A linked card. */
export default function CardLink2({ d, cids, styles }: { d: CardLink2Data; cids: string[]; styles: CardLink2Styles }) {
  return (
    <a data-cid={cids[0]} className="h-18 block p-3 rounded-lg cursor-pointer hover:bg-border" data-component="link" href={d.href}>
      <div data-cid={cids[1]} className="h-12 flex items-center gap-3">
        <img data-cid={cids[2]} className="border border-solid border-color-002 block max-w-full rounded-lg overflow-clip object-cover align-middle w-12 h-12" data-component="image" alt={d.alt} src={d.imgSrc} />
        <div data-cid={cids[3]} className={cn("h-12 block min-w-0 flex-1 max-md:w-36.5 md:max-lg:w-[6.6625rem] 2xl:w-[17.0375rem]", styles.className)}>
          <div data-cid={cids[4]} className={cn("flex items-center gap-2 max-md:w-36.5 md:max-lg:w-[6.6625rem] 2xl:w-[17.0375rem]", styles.className2)}>
            <h3 data-cid={cids[5]} className={cn("block overflow-hidden text-color-001 font-semibold whitespace-nowrap text-nowrap", styles.className3)} data-component="heading">
              {d.title}
            </h3>
          </div>
          <p data-cid={cids[6]} className="h-8 overflow-hidden text-muted-foreground text-[0.75rem] line-clamp-2">
            {d.description}
          </p>
        </div>
        <div data-cid={cids[7]} className="h-8.5 border border-solid border-border flex relative py-1 px-[0.9375rem] rounded-lg justify-center items-center gap-1 text-color-001 text-sm leading-5.5 text-center whitespace-nowrap text-nowrap bg-color-003 hover:bg-border" data-component="button" type="button">
          <span data-cid={cids[8]} className="block">
            Install
          </span>
        </div>
      </div>
    </a>
  );
}
