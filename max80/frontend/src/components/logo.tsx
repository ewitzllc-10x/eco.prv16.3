import type { LogoStyles } from "../_styles";
import { cn } from "../../lib/utils";
export type LogoData = {
  alt: string;
  imgSrc: string;
};
/** A logo. */
export default function Logo({ d, cids, styles }: { d: LogoData; cids: string[]; styles: LogoStyles }) {
  return (
    <img data-cid={cids[0]} className={cn("block max-w-full overflow-clip object-contain align-middle h-6", styles.className)} data-component="image" alt={d.alt} src={d.imgSrc} />
  );
}
